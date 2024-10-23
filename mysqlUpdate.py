import mysql.connector
myFirstdb = mysql.connector.connect(host="localhost",user="root",password="system",database="sivasivanidc")
mycursor=myFirstdb.cursor()
sql = "UPDATE student SET address = 'sdpt' WHERE htno = '102'"

mycursor.execute(sql)


myFirstdb.commit()

print(mycursor.rowcount, "record(s) affected")
