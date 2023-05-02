# after installations the real job starts

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'LIlian080'

)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database 
cursorObject.execute("CREATE DATABASE hilarydb")

print('All Done!')