import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SYSTEM",
  database="ssdc_test"
)

mycursor = mydb.cursor()

sql = "INSERT INTO BScCSE(name, address) VALUES (%s, %s)"
val = ("Ram", "Kompally")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
#mysql> select *from bsccse;
