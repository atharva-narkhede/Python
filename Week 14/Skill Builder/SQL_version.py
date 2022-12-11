#Write a program to connect to the SQL database from python and print its version.
#The connection details are given below:
#HOST: localhost DB:rootuser
#Default USER: rootuser Default PWD: rootuser


import pymysql
def getDbConnection():
    connection = pymysql.connect('localhost','rootuser','rootuser','rootuser')
    return connection

def closeDbConnection(connection):
    connection.close()

def readDbVersion():

    connection = getDbConnection()
    db_Info = connection.get_server_info()
    print(db_Info)
    closeDbConnection(connection)

readDbVersion()

