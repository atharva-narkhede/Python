#Write a program to connect to the database from python and write a query to display all the employee names and their salary(name, salary) whose bonus is less than or equal to the given bonus. Sort the output by ascending order of name.
#Import pymysql module to connect to the database.


import pymysql
def getDbConnection():
    connection = pymysql.connect('localhost','rootuser','rootuser','rootuser')
    return connection

def closeDbConnection(connection):
    connection.close()

def getResult(SqlQuery,bonus_ref):
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute(SqlQuery,(bonus_ref))
    records = cursor.fetchall()
    for record in records:
        print(record)
    closeDbConnection(connection)


SqlQuery = "select name,salary from employee e, bonus b where e.empid = b.empid and b.bonus <= %s order by name;"

bonus_ref = float(input())

getResult(SqlQuery,bonus_ref)
    
