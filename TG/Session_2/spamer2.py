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

from messages2 import MESSAGES


api_id = 16497622
api_hash = 'bd832c582aa57668ed889a5e2cd273cb'
phone='62895383484324'

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
