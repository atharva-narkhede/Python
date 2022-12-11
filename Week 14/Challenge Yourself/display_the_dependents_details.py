#Write a program to connect to the database from python and write a query to display the dependents details (first_name, last_name, relationship) for the given employee_id.
#Import pymysql module to connect to the database.


import pymysql
def getDbConnection():
    connection = pymysql.connect('localhost','rootuser','rootuser','rootuser')
    return connection

def closeDbConnection(connection):
    connection.close()

def getResult(SqlQuery,emp_id):
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute(SqlQuery,(emp_id))
    records = cursor.fetchall()
    for record in records:
        print(record)
    closeDbConnection(connection)

 
SqlQuery = "select d.first_name, d.last_name, d. relationship FROM dependents d where employee_id = %s;"

emp_id = int(input())


getResult(SqlQuery,emp_id)
    

