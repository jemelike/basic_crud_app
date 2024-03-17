import os
import psycopg2

DATABASE_USER = os.environ['POSTGRES_USER']
DATABASE_PASSWORD = os.environ['POSTGRES_PASSWORD']
DATABASE_HOST = os.environ['']
DATABASE_PORT = os.environ
DATABASE_NAME =  os.environ
conn = psycopg2.connect(database=DATABASE_NAME, user=DATABASE_USER, 
                        password=DATABASE_PASSWORD, host=DATABASE_HOST, port=DATABASE_PORT) 

class Service():
    pass