#Write a program to connect to database from python and write a query to fetch the number of doctors for a given 'Speciality' 
#Import pymysql module to connect to the database.


import pymysql
def getDbConnection():
    connection = pymysql.connect('localhost','rootuser','rootuser','rootuser')
    return connection

def closeDbConnection(connection):
    connection.close()

def getResult(SqlQuery,Speciality):
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute(SqlQuery,(Speciality))
    records = cursor.fetchone()
    for record in records:
        print(record)
    closeDbConnection(connection)

Speciality = input()

SqlQuery = "SELECT COUNT(*) FROM Doctor_Info WHERE Speciality = %s;"
getResult(SqlQuery,Speciality)
    
