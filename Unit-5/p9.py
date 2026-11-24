import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mca1a"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS customers(name VARCHAR(20), city VARCHAR(20))")

sql = "INSERT INTO customers VALUES(%s, %s)"
val = [
    ("Jayesh", "Rajkot"),
    ("Ramesh", "Mumbai"),
    ("Amit", "Ahmedabad")
]

mycursor.executemany(sql, val)
mydb.commit()

print("Records inserted successfully")

mycursor.execute("SELECT * FROM customers")
print("\nUsing fetchone():")
print(mycursor.fetchone())

mycursor.execute("SELECT * FROM customers")
print("\nUsing fetchmany():")
print(mycursor.fetchmany(2))

mycursor.execute("SELECT * FROM customers")
print("\nUsing fetchall():")
print(mycursor.fetchall())

mydb.close()