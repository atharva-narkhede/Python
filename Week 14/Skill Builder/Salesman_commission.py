#Write a program to connect to database from python and write a query to find those salesmen who get the commission greater than or equal to given range (inclusive of given range). Sort the output by ascending order of salesman_id.
#Import pymysql module to connect to the database.

import pymysql
def getDbConnection():
    connection = pymysql.connect('localhost','rootuser','rootuser','rootuser')
    return connection

def closeDbConnection(connection):
    connection.close()

def getResult(SqlQuery,commission):
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute(SqlQuery,(commission))
    records = cursor.fetchall()
    for record in records:
        print(record)
    closeDbConnection(connection)


SqlQuery = "select salesman_id, name, city, commission from salesman where commission >= %s order by 1"

commission = float(input())

getResult(SqlQuery,commission)
    
