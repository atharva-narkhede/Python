#Given 2 Tables Hospital and Doctor. Connect to the database from Python and fetch the number of doctors corresponding to each hospital(Hospital_Name, Number of doctors). Sort the output by ascending order of hospital name.
#Import pymysql module to connect to database.

import pymysql
def getDbConnection():
    connection = pymysql.connect('localhost', 'rootuser', 'rootuser', 'rootuser')
    return connection

def closeDbConnection(connection):
    connection.close()

def getResult(SqlQuery):
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute(SqlQuery)
    records = cursor.fetchall()
    for record in records:
        print(record)
    closeDbConnection(connection)


SqlQuery = "SELECT A.Hospital_Name, count(*) from Hospital A join Doctor B on A.Hospital_Id = B.Hospital_Id group by B.Hospital_Id order by 1;"
getResult(SqlQuery)
    
