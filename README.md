![logo](/images/greengrass.png)
# AWS Greengrass Workshop

## Introduction
Greengrass is a software that allows you to extend AWS cloud capabilities to local devices, making it possible to collect data and securely communicate with local network and AWS Cloud. Fits very well for IoT solutions as gateway that need to communicate with Bluetooth, Zigbee or any other type of device communication.

![More information about Green Grass](https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html)


## Table of Content

* [Configure your Raspberry Pi](#1configure-permissions-and-raspberry-pi)
* [Configure AWS Permissions](#2create-your-own-lambda-function-to-your-alexa-skill)
* [Create Greengrass Group](#3create-your-own-dynamodb-table)
* [Deploy your First Lambda to your Raspberry Pi](#4customizing-nursing-skill)
* [Reading Bluetooth Blood Pressure Sensor](#4customizing-nursing-skill)

## 1.Configure Permissions and Raspberry Pi

Before we start using Greengrass we need to configure our Raspberry PI AWS credentials for awscli and also be sure you have access to your Pi using SSH.

### Step #1: Open IAM Console to create an access key
![screen](/images/raspberry-config/01.png) 

### Step #2: Click in your AWS user
![screen](/images/raspberry-config/02.png) 

### Step #3: Click "Security Credentials"
![screen](/images/raspberry-config/03.png) 

### Step #4: Click "Create Access Key" 
![screen](/images/raspberry-config/04.png) 

### Step #5: Copy the Access Key ID and Secret Access

You can also download a CSV file with your keys!
![screen](/images/raspberry-config/05.png) 

### Step #6: Access your Raspberry Pi using SSH and configure awscli

* Open ssh: ssh pi@RASP-IP-ADDRESSS
* Type: aws configure
* Enter your keys
* Choose us-east-1 as region
* Choose json as output

![screen](/images/raspberry-config/06.png) 

### Step #7: Select your User  
![screen](/images/raspberry-config/07.png) 

### Step #8: Click "Add permissions"
![screen](/images/raspberry-config/08.png) 

### Step #9: Click "Attach existing policies directly"
![screen](/images/raspberry-config/09.png) 

### Step #10: Choose "AdministratorAccess"  
![screen](/images/raspberry-config/10.png) 

### Step #11: Choose "AmazonDynamoDBFullAccess"
![screen](/images/raspberry-config/11.png) 

### Step #12: Choose "AWSGreengrassFullAccess"
![screen](/images/raspberry-config/12.png) 

### Step #13: Choose "AWSIoTFullAccess" and click "Next Review"
![screen](/images/raspberry-config/13.png) 

### Step #14: Click "Add permission" and done!
![screen](/images/raspberry-config/14.png) 

