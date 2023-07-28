import mysql.connector

from dotenv import load_dotenv

import os

load_dotenv()

database = mysql.connector.connect(
    host = os.environ.get('MY_HOST'),
    user = os.environ.get('MY_USER'),
    password = os.environ.get('MY_PASSWORD')
)

# Prepare a cursor objects

cursorObject = database.cursor()

# create a database

cursorObject.execute("CREATE DATABASE farmdb")


print("Good Job, al done!!!")