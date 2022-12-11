#Write a program to connect to database from python and write a query to display product_name and quantity_per_unit whose unit_price is greater than the given price. Sort the output by ascending order of product name.
#Import pymysql module to connect to the database.

import pymysql
def getDbConnection():
    connection = pymysql.connect('localhost','rootuser','rootuser','rootuser')
    return connection

def closeDbConnection(connection):
    connection.close()

def getResult(SqlQuery,price):
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute(SqlQuery,(price))
    records = cursor.fetchall()
    for record in records:
        print(record)
    closeDbConnection(connection)


SqlQuery = "select product_name, quantity_per_unit from products where unit_price >  %s order by product_name"

price = float(input())

getResult(SqlQuery,price)
    

