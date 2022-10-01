import cmd
from email import message
from telethon import TelegramClient, sync
from os import system
import time
from time import sleep
#from users import USERS
#pip install alive_progress
from alive_progress import alive_bar
#pip install tqdm
from tqdm import tqdm, trange
import csv
import asyncio

from messages1 import MESSAGES


api_id = 11032936
api_hash = '55410e3b89b52d2bb49fac10b8052f34'
phone='79919537697'

print()
print('Connecting to the session ' + phone)
client = TelegramClient(phone, api_id, api_hash)
client.connect()
client.start()
print()

messages = MESSAGES
with open('data_base.csv', newline = '') as USERS:
    Count = 40
    for user in tqdm(USERS, total = Count):
        reader = csv.DictReader(USERS)
        client.send_message(user, messages)
        sleep(1)
        time.sleep(1)

