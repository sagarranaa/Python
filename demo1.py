import mysql.connector # this is mysql connector to database
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Sagar@77",database="student")
mycursor=mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)