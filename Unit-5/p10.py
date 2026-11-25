import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mca1a"
)

mycursor = mydb.cursor(buffered=True)

mycursor.execute("SELECT * FROM student")
print("\nUsing fetchone():")
print(mycursor.fetchone())

mycursor.execute("SELECT * FROM student")
print("\nUsing fetchmany():")
print(mycursor.fetchmany(2))

mycursor.execute("SELECT * FROM student")
print("\nUsing fetchall():")
print(mycursor.fetchall())

mydb.close()
