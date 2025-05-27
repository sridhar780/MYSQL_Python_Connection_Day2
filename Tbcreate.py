import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SYSTEM",
  database="ssdc_test"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE BScCSE (name VARCHAR(255), address VARCHAR(255))")
#mysql> use ssdc_test;
#mysql> show tables;
