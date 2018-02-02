![logo](/images/greengrass.png)
# AWS Healthcare Greengrass Workshop

## Introduction
![logo](/images/gg1.png)
Greengrass is a software that allows you to extend AWS cloud capabilities to local devices, making it possible to collect data and securely communicate with local network and AWS Cloud. Fits very well for IoT solutions as gateway that could handle communication with Bluetooth, Zigbee devices, for example.

![More information about Green Grass](https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html)

###Greengrass Group, Core and Devices

![logo](/images/gg2.png)


## Table of Content

* [Configure your Raspberry Pi](#1configure-permissions-and-raspberry-pi)
* [Create Lambda Function](#2create-a-lambda-function)
* [Create Greengrass Group](#3create-greengrass-group)
* [Deploy Lambda to your Raspberry Pi](#4deploy-lambda-to-your-raspberry-pi)
* [Monitoring and Processing AWS IoT Messages](#5monitoring-and-processing-aws-iot-messages)
* [Greengrass Controlling Bluetooth Blood Pressure Sensor](#6greengrass-controlling-bluetooth-blood-pressure-sensor)

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

### Step #1: Open Lambda Console and click "Create a function"
![screen](/images/lambda/01.png) 

### Step #2: Select "Author from scratch"
* Name: healthcare-data-generator
* Runtime: Python 2.7
* Existing Role: lambda_basic_execution

![screen](/images/lambda/02.png) 

### Step #3: Scroll down to Function code panel

* Download ![this .ZIP project](https://github.com/InternetOfHealthcare/greengrass/raw/master/src/healthcare-data-generator.zip) to your machine
* Select "Upload a .ZIP file" in "Code entry type" combo

![screen](/images/lambda/03.png) 

### Step #4: Click "Upload" and select the .ZIP file downloaded in the previous step and then click "Save"
![screen](/images/lambda/04.png) 

### Step #5: Select "Edit code line" in "Code entry type" to see the Lambda code
![screen](/images/lambda/05.png) 

### Step #6: Click "Actions -> Publish new version" 
![screen](/images/lambda/06.png) 

### Step #7: Name it "v1" and done! 
![screen](/images/lambda/07.png) 


## 3.Create Greengrass Group

It's time to create a Greengrass Group that represents our Raspberry Pi as a Core Device.

### Step #1: Open Greengrass console and click "Get started" to create a group
![screen](/images/greengrass-group/01.png) 

### Step #2: Select "Use easy creation"
![screen](/images/greengrass-group/02.png) 

### Step #3: Name your group as "healthcare"
![screen](/images/greengrass-group/03.png) 

### Step #4: Accept the suggested core name
![screen](/images/greengrass-group/04.png) 	

### Step #5: Click "Create group and core"
![screen](/images/greengrass-group/05.png) 

### Step #6: Click "Download these resoures as .tar.gz"
![screen](/images/greengrass-group/06.png) 

### Step #7: Download Greengrass security resources to your machine
![screen](/images/greengrass-group/07.png) 

### Step #8: Click "Finish"
![screen](/images/greengrass-group/08.png) 

### Step #9: Access your Raspberry Pi and type this command to create a fresh Greengrass core
![screen](/images/greengrass-group/09.png) 

### Step #10: Type "cd greengrass"
![screen](/images/greengrass-group/10.png) 

### Step #11: Upload your .tar.gz security resources file and uncompress into Greengrass directory
![screen](/images/greengrass-group/11.png) 

### Step #12: Type these commands to copy the root.ca.pem certificatre
![screen](/images/greengrass-group/12.png) 

### Step #13: Now you can start your Greengrass core!
![screen](/images/greengrass-group/13.png) 

## 4.Deploy Lambda to your Raspberry Pi

Let's deploy our Lambda function to run locally in our Raspberry Pi.

### Step #1: Open Greengrass console, select "healthcare" group and click "Lambdas"
![screen](/images/greengrass-deployment/01.png) 

### Step #2: Select "Use existing Lambda"
![screen](/images/greengrass-deployment/02.png) 

### Step #3: Select "helthcare-data-generator" Lambda
![screen](/images/greengrass-deployment/03.png) 

### Step #4: Select the published version
![screen](/images/greengrass-deployment/04.png) 

### Step #5: Click "Edit configuration"
![screen](/images/greengrass-deployment/05.png) 

### Step #6: Change Lambda Life-cycle to Long-lived function
![screen](/images/greengrass-deployment/06.png) 

### Step #7: Your configuration should be like this
![screen](/images/greengrass-deployment/07.png) 

### Step #8: Back to healthcare group and click "Subscriptions"
![screen](/images/greengrass-deployment/08.png) 

### Step #12: Select "Lambdas -> healthcare-data-genertor" as Source
![screen](/images/greengrass-deployment/12.png) 

### Step #13: Selecr "IoT Cloud" as Target
![screen](/images/greengrass-deployment/13.png) 

### Step #14: With this subscrition our Lambda will be able to reach any topic in the Cloud
![screen](/images/greengrass-deployment/14.png) 

### Step #15: Click finish
![screen](/images/greengrass-deployment/15.png) 

### Step #16: Now let's deploy by clicking "Actions -> Deploy"  menu
![screen](/images/greengrass-deployment/16.png) 

### Step #17: Click "Automatic detection"
![screen](/images/greengrass-deployment/17.png) 

### Step #18: Grant the required permissions
![screen](/images/greengrass-deployment/18.png) 

### Step #19: In Group Role click "Add role" link
![screen](/images/greengrass-deployment/19.png) 

### Step #20: Choose "Greengrass_ServiceRole" and click "Save"
![screen](/images/greengrass-deployment/20.png) 

### Step #21: Now let's do the final deploy, click "Actions -> Deploy" again
![screen](/images/greengrass-deployment/21.png) 

### Step #22: You should see "Successfully completed message"
![screen](/images/greengrass-deployment/22.png) 

## 5.Monitoring and Processing AWS IoT Messages

Now it's time to monitor AWS IoT to check for incoming MQTT messages from your Raspberry Pi.

### Step #1: Open AWS IoT Console
![screen](/images/iot-messages/01.png) 

### Step #2: Click "Test" and then subscribe to healthcare/data topic
![screen](/images/iot-messages/02.png) 

### Step #3: You should start seeing health data generated by Greengrass / Raspi
![screen](/images/iot-messages/03.png) 

### Step #4: Now let's start processing this data 

* Open Lambda console and create a new Lambda
* Name: Healthcare-Data-JSONToDynamoDB

![screen](/images/iot-messages/04.png) 

### Step #5: Use the following code
* ![Lambda Code](https://github.com/InternetOfHealthcare/greengrass/blob/master/src/Healthcare-data-JSONToDynamoDB.js)
![screen](/images/iot-messages/05.png) 

### Step #6: Open IoT Console and click "Act"
![screen](/images/iot-messages/06.png) 

### Step #7: Click "Create a rule"

* This rule will trigger our lambda function for each message received on healthcare/data topic
* Name: HealthData
![screen](/images/iot-messages/07.png) 

### Step #8: As topic filter, type healthcare/data
![screen](/images/iot-messages/08.png) 

### Step #9: Add an action and select Lambda
![screen](/images/iot-messages/09.png) 

### Step #10: Select your lambda function and done!

* After you finish this, your healthcare data will be stored on DynamoDB, let's check it!
![screen](/images/iot-messages/10.png) 

### Step #11: Open DynamoDB Console
![screen](/images/iot-messages/11.png) 

### Step #12: Click "Tables", choose the "patient" table and click "Items"
* If you can see the data coming to the data, congrats, evertything is working!
![screen](/images/iot-messages/12.png) 


## 6.Greengrass Controlling Bluetooth Blood Pressure Sensor

