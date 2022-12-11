#Write a program to connect to the database from python and write a query to display the column area_million_sqkm whose country_name is given as input.
#Import pymysql module to connect to the database.


import pymysql
def getDbConnection():
    connection = pymysql.connect('localhost','rootuser','rootuser','rootuser')
    return connection

def closeDbConnection(connection):
    connection.close()

def getResult(SqlQuery,country):
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute(SqlQuery,(country))
    records = cursor.fetchone()
    for record in records:
        print(record)
    closeDbConnection(connection)


SqlQuery = "select area_million_sqkm  from world where country_name = %s;"

country = input()

getResult(SqlQuery,country)
    
