'''
Adding Timestamps
=================

You can add timestamps to your log messages by simply by including the timestamp in the message string.
'''

import logging
import datetime
import time
import subprocess

# clear log file
subprocess.call("rm logs/example.log", shell=True)

t = time.mktime(time.localtime())
t = time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))

# set the root logger
LOG_FILENAME = 'logs/example.log'

# set debug level
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

# log some messages
logging.debug('This message goes to the log file')
logging.info(f'This message was timed at: {t}')   # timestamp included in message

# inspect log file
import os
os.system("cat logs/example.log")

subprocess.call("cat logs/example.log", shell=True)