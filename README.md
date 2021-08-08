# TechConf Conference Platform, Azure Non-Native App Deployment And Migration

## Table of Contents

- [Summary](#Summary)

- [Technologies](#Technologies)

- [Sample Data](#Sample-Data)

- [Structure](#Structure)

- [Monthly Cost Analysis](#Monthly-Cost-Analysis)

- [Architecture Explanation](#Architecture-Explanation)

- [Configuration](#Configuration)

- [Deployment](#Deployment)

## Summary

This TechConf website was configured, migrated and deployed to Azure as part of my **Cloud Developer using Microsoft Azure Nanodegree from Udacity**.

**It demonstrates my understanding and ability to configure the following :**

#### Azure services

Azure Webjobs.  
Azure Functions.  
Azure Service Bus.  
Azure App Service.  
Azure Service Bus Queues.  
Azure Postgres Database server.

#### Development

Create an Azure notification function and configure it to trigger with the service bus queue.  
Configuring and communicating with the queueing service using Microsoft's Queue_Client library.   
Configure the notifications endpoint to communicate with both the queueing service and the PostgreSQL database.

#### Migration

Azure Batch.   
Azure Lift & Shift.   
Azure SQL Migration.   
Azure PostgreSQL Migration.
Azure Database Migration Service.   


#### Deployment

Deploy and migrate a client side web app (Azure App Service).   
Deploy and migrate a postgreSQL server (Azure Postgres Database server).   
Deploy and migrate a notification function that sends emails to attendees (Azure Service Bus).


## Technologies
[Arcana static frontend.](https://html5up.net/arcana)    
Flask was used for the backend.  
Python was used as the language of choice.   
SQLAlchemy was used as the ORM of choice.  
Azure App Service was used for hosting the app.    
Azure Service Bus was for the notification queue.  
Azure Database was used for the PostgreSQL server.  
Azure Functions was used for the notification function deployment.   

## Sample Data

Two PostgreSQL migration backups are available at /data

## Structure

```
|   README.md
|
+---data
|       techconfdb_backup.sql
|       techconfdb_backup.tar
|
+---function
|   |   requirements.txt
|   |
|   \---ServiceBusQueueFunction
|           function.json
|           sample.dat
|           __init__.py
|
+---screenshots
|   |   README.md
|   |
|   +---Migrate Background Process
|   |       1.PNG
|   |       2.PNG
|   |       3.PNG
|   |       4.PNG
|   |
|   +---Migrate Database
|   |       1.PNG
|   |       2.PNG
|   |
|   \---Migrate Web Applications
|           1.PNG
|           2.PNG
|
\---web
    |   .gitignore
    |   application.py
    |   config.py
    |   requirements.txt
    |
    \---app
        |   models.py
        |   routes.py
        |   __init__.py
        |
        +---static
        |   +---css
        |   |   |   fontawesome-all.min.css
        |   |   |   main.css
        |   |   |
        |   |   \---images
        |   |           bg01.png
        |   |           bg02.png
        |   |           bg03.png
        |   |
        |   +---images
        |   |       banner.jpg
        |   |       banner2.jpg
        |   |       favicon.ico
        |   |       pic01.jpg
        |   |       pic010.jpg
        |   |       pic02.jpg
        |   |       pic020.jpg
        |   |       pic03.jpg
        |   |       pic030.jpg
        |   |       pic04.jpg
        |   |       pic040.jpg
        |   |
        |   +---js
        |   |       breakpoints.min.js
        |   |       browser.min.js
        |   |       jquery.dropotron.min.js
        |   |       jquery.min.js
        |   |       main.js
        |   |       util.js
        |   |
        |   \---webfonts
        |           fa-brands-400.eot
        |           fa-brands-400.svg
        |           fa-brands-400.ttf
        |           fa-brands-400.woff
        |           fa-brands-400.woff2
        |           fa-regular-400.eot
        |           fa-regular-400.svg
        |           fa-regular-400.ttf
        |           fa-regular-400.woff
        |           fa-regular-400.woff2
        |           fa-solid-900.eot
        |           fa-solid-900.svg
        |           fa-solid-900.ttf
        |           fa-solid-900.woff
        |           fa-solid-900.woff2
        |
        \---templates
                attendees.html
                base.html
                index.html
                notification.html
                notifications.html
                registration.html
```

## Monthly-Cost-Analysis

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure Postgres Database* | Basic - Single Server - 1 vCore - 5GB | 25.32 USD |
| *Azure Service Bus* | Basic - 256KB Max Message Size - Shared Capacity | 0.05 USD |
| *Azure App Service* | Free - F1 - 1GB Memory | 0.0 USD |
| *Azure Functions* | Free 1 Million Executions- Price Per Million Afterwards: | 0.20 USD |

Current prices are based on both my own observations [and The official Azure pricing dashboard.](https://azure.microsoft.com/en-us/pricing/)  

## Architecture-Explanation

This project was architectured with cost and performance in mind, after considering the small size of our application and our lack of needing a dynamic website allows us to pick a free Azure app service.   
Splitting our notification and database into their own services allows us to:
1. Scale only the services that need scaling in case of an influx of usage.
2. And still being able to only pay according to our usage.   

Thus our solution brings us the best features in terms of cost, scalability and even performance.

## Configuration

You will have to configure/use the following services

1. Azure Functions.  
2. Azure Service Bus.  
3. Azure App Service.  
4. Azure Service Bus Queues.  
5. Azure Postgres Database server.

Make the following changes to the files located at 

### Look for


```python
POSTGRES_SERVER_URL
POSTGRES_SERVER_USER 
POSTGRES_SERVER_PASSWORD 
DB_NAME_HERE
```
### In the following locations :

#### 1. web/config.py 

#### 2. function/ServiceBusQueueFunction/__init__.py

### And replace it with

Your Azure PostgreSQL server and database info

## Deployment

Install the following

- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
- [Azure Function tools V3](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash#install-the-azure-functions-core-tools)
- [Azure Tools for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack)

### 1. Web App

Use the following command to deploy your frontend to Azure App Service

```shell
az webapp up --sku F1 -n <APP_NAME> --resource-group <RESOURCE_GROUP_NAME>
```

### 2. Service Bus Queue

Create a Service Bus resource with a notificationqueue that will be used to communicate between the web and the function

### 2. Notification Function

create an Azure Function in the function folder that is triggered by a service bus queue.   
You will need to copy/paste and replace the **__init.py__** file in your newly created Azure function folder with the __init.py__ file included with this project that's located in the function/ServiceBusQueueFunction folder.   

Publish the Azure Function