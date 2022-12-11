#Given a table, Salesman. Connect to database from Python and display names and city of salesman (name, city) for the given city.
#Import pymysql module to connect to database.
#Sort the output by ascending order of names of a salesman.


import pymysql
def getDbConnection():
    connection = pymysql.connect('localhost', 'rootuser', 'rootuser', 'rootuser')
    return connection

def closeDbConnection(connection):
    connection.close()

def getResult(SqlQuery,cityname):
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute(SqlQuery,(cityname))
    records = cursor.fetchall()
    for record in records:
        print(record)
    closeDbConnection(connection)


cityname = input()
SqlQuery = "SELECT name,city FROM Salesman WHERE city = %s order by 1;"
getResult(SqlQuery,cityname)
    
