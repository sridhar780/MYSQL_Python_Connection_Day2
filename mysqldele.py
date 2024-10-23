import mysql.connector
myFirstdb = mysql.connector.connect(host="localhost",user="root",password="system",database="sivasivanidc")
mycursor=myFirstdb.cursor()
sql = "DELETE FROM student WHERE address = 'hyd'"

mycursor.execute(sql)

myFirstdb.commit()

print(mycursor.rowcount, "record(s) deleted")
