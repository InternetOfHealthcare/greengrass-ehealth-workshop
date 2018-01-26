![logo](/images/greengrass.png)
# AWS Healthcare Greengrass Workshop

## Introduction
Greengrass is a software that allows you to extend AWS cloud capabilities to local devices, making it possible to collect data and securely communicate with local network and AWS Cloud. Fits very well for IoT solutions as gateway that need to communicate with Bluetooth, Zigbee or any other type of device communication.

![More information about Green Grass](https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html)


## Table of Content

* [Configure your Raspberry Pi](#1configure-permissions-and-raspberry-pi)
* [Create Lambda Function](#2create-lambda-function)
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

### Step #7: Return to IAM Console and select your user  
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

### Step #14: Click "Add permissions" and done!
![screen](/images/raspberry-config/14.png) 

## 2.Create a Lambda Function

Now we are going to create a Lambda function that we will deploy to our Raspberry Pi later. This Lambda will be sending simulated blood pressure data.

### Step #1: 
![screen](/images/lambda/01.png) 

### Step #2: 
![screen](/images/lambda/02.png) 

### Step #3: 
![screen](/images/lambda/03.png) 

### Step #4: 
![screen](/images/lambda/04.png) 

### Step #5: 
![screen](/images/lambda/05.png) 

### Step #6: 
![screen](/images/lambda/06.png) 

### Step #7: 
![screen](/images/lambda/07.png) 

### Step #8: 
![screen](/images/lambda/08.png) 

### Step #9: 
![screen](/images/lambda/09.png) 

### Step #10: 
![screen](/images/lambda/10.png) 

### Step #11: 
![screen](/images/lambda/11.png) 


## 3.Create Greengrass Group

It's time to create a Greengrass Group that represents our Raspberry Pi as a Core Device.

### Step #1: 
![screen](/images/greengrass-group/01.png) 

### Step #2: 
![screen](/images/greengrass-group/02.png) 

### Step #3: 
![screen](/images/greengrass-group/03.png) 

### Step #4: 
![screen](/images/greengrass-group/04.png) 

### Step #5: 
![screen](/images/greengrass-group/05.png) 

### Step #6: 
![screen](/images/greengrass-group/06.png) 

### Step #7: 
![screen](/images/greengrass-group/07.png) 

### Step #8: 
![screen](/images/greengrass-group/08.png) 

### Step #9: 
![screen](/images/greengrass-group/09.png) 

### Step #10: 
![screen](/images/greengrass-group/10.png) 

### Step #11: 
![screen](/images/greengrass-group/11.png) 

### Step #12: 
![screen](/images/greengrass-group/12.png) 

### Step #13: 
![screen](/images/greengrass-group/13.png) 

