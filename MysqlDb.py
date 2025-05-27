import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SYSTEM"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Ssdc_Test")
