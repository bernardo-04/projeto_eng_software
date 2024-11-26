from dotenv import load_dotenv
from psycopg import pool
import os

load_dotenv()

connection = pool.SimpleConnectionPool(
    1,
    10,
    dbname=os.getenv("DATABASE_NAME"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    port=os.getenv("DATABASE_PORT")
)

def getConnection():
    return connection.getconn()

def releaseConnection(activeConnection):
    return connection.putconn(activeConnection)

def closeAllConnections():
    connection.closeall()