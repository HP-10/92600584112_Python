import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mca1a"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS student(sid int, name VARCHAR(20), city VARCHAR(20))")

mycursor.execute("INSERT INTO student VALUES(101, 'Jayesh', 'Morbi')")
mycursor.execute("INSERT INTO student VALUES(102, 'Ramesh', 'Mumbai')")
mycursor.execute("INSERT INTO student VALUES(103, 'Kalpesh', 'Rajkot')")
mycursor.execute("INSERT INTO student VALUES(104, 'Raju', 'Jamanagar')")
mycursor.execute("INSERT INTO student VALUES(105, 'Hemang', 'Morbi')")

mydb.commit()

print("Records inserted successfully")

mycursor.execute("SELECT * FROM student")

for x in mycursor:
    print(x)

mydb.close()