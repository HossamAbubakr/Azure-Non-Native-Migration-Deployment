import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode("utf-8"))
    logging.info(f"Python ServiceBus queue trigger processed message: {notification_id}")
    # DONE: Get connection to database
    dbCon = psycopg2.connect(dbname="DB_NAME_HERE", user="POSTGRES_SERVER_USER", password="POSTGRES_SERVER_PASSWORD", host="POSTGRES_SERVER_URL")
    cur = dbCon.cursor()
    print("Connection established")
    try:
        # DONE: Get notification message and subject from database using the notification_id
        notif_query = cur.execute(f"SELECT message, subject FROM notification WHERE id = {notification_id};")
        event_notification = cur.fetchone()
        print("Executed query on notifications")
        # DONE: Get attendees email and name
        attend_query = cur.execute("SELECT first_name, last_name, email FROM attendee;")
        all_attendees = cur.fetchall()
        print("Executed query on attendees")
        # DONE: Loop through each attendee and send an email with a personalized subject
        # As per : https://docs.sendgrid.com/for-developers/sending-email/v3-python-code-example
        for attendee in all_attendees:
            message = Mail(
            from_email="admin@techconf.com",
            to_emails=attendee[2],
            subject="You have a notification.",
            html_content=f"<b>You have a notification for the following {event_notification}</b>"
            )
            # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            # response = sg.send(message)
        print(f"Sent emails to {len(all_attendees)} attendees")
        # DONE: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        completed_date = datetime.utcnow()
        status = f"Notified {len(all_attendees)} attendees"
        update_notif_query = cur.execute(f"UPDATE notification SET completed_date = {completed_date}, status = {status} WHERE id = {notification_id};")
        dbCon.commit()
        print("Executed notification update query")
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        cur.close()
        dbCon.close()