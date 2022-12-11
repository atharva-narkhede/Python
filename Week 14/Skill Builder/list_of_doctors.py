#Write a program to connect to database from python and write a query to get the list of doctors(Doctor_Id, Doctor_Name, Hospital_Id) as per the given Speciality and Salary greater than the given salary. 
#Sort the output by ascending order of Doctor_Id. 
#Import pymysql module to connect to the database.


import pymysql
def getDbConnection():
    connection = pymysql.connect('localhost','rootuser','rootuser','rootuser')
    return connection

def closeDbConnection(connection):
    connection.close()

def getResult(SqlQuery,Speciality,Salary):
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute(SqlQuery,(Speciality, Salary))
    records = cursor.fetchall()
    for record in records:
        print(record)
    closeDbConnection(connection)


SqlQuery = "select Doctor_Id, Doctor_Name, Hospital_Id from Doctor_Info where Speciality=%s and Salary > %s order by 1"
Speciality = input()
Salary = float(input())

getResult(SqlQuery,Speciality,Salary)
    
