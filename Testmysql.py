import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SYSTEM"
)

print(mydb)
#mysql> show databases;
#mysql> SELECT user,host FROM mysql.user;
