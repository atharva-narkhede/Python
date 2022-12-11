#Write a program to connect to database from python and write a query to find those salesmen whose first name is equal to the given string. Sort the output by ascending order of last_name. 
#Import pymysql module to connect to the database.


import pymysql
def getDbConnection():
    connection = pymysql.connect('localhost','rootuser','rootuser','rootuser')
    return connection

def closeDbConnection(connection):
    connection.close()

def getResult(SqlQuery,firstname):
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute(SqlQuery,(firstname))
    records = cursor.fetchall()
    for record in records:
        print(record)
    closeDbConnection(connection)


SqlQuery = "select salesman_id, first_name,last_name, city, commission from salesman where first_name =  %s order by last_name"

firstname = input()

getResult(SqlQuery,firstname)
    
