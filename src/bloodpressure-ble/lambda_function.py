import greengrasssdk
import platform
from threading import Timer
import time
import sys
import logging
import json
import datetime
import pexpect
import os



# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
DEVICE = "A4:D5:78:13:E4:63"
client = greengrasssdk.client('iot-data')
my_platform = platform.platform()

def function_handler(event, context):
        logger.info("Received message!")
        bp_trigger();

def bp_trigger():
    child = pexpect.spawn("gatttool -I")
    child.sendline("connect {0}".format(DEVICE))
    child.expect("Connection successful", timeout=5)
    child.sendline("char-write-cmd 0x0012 65")
    child.expect("Notification handle = 0x0012 value: 67 2f ", timeout=35)
    bphex = child.readline()
    child.sendline("disconnect")
    child.close()
    logger.info(bphex)
    timestamp = str(time.time())
    nums = bphex.split()
    systolic = int(str(int(nums[0],16) - 48) + str(int(nums[1],16) - 48) + str(int(nums[2],16) - 48))
    diastolic = int(str(int(nums[4],16) - 48) + str(int(nums[5],16) - 48) + str(int(nums[6],16) - 48))
    bpm = int(str(int(nums[8],16) - 48) + str(int(nums[9],16) - 48) + str(int(nums[10],16) - 48))
    bpjson = '{"data_id" : "bp", "ts" : "' + timestamp + '", "systolic" : ' + str(systolic) + ',"diastolic" : ' + str(diastolic) + ',"bpm" : ' + str(bpm) + '}'
    logger.info("Sending json to AWS MQTT" + bpjson)
    client.publish(topic='healthcare/data', payload=bpjson)
    speak = '{ "message" : "Your systolic pressure is ' + str(systolic) + ' diastolic is ' + str(diastolic) + ' and your heart beat is ' + str(bpm) + ' beats per minute"'
    client.publish(topic='polly', payload = speak)
    