import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
import pandas as pd

load_dotenv()

hn = os.environ['DATABASE_HOST']
un = os.environ['DATABASE_USER']
pw = os.environ['DATABASE_PW']

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

create_server_connection(hn, un, pw)