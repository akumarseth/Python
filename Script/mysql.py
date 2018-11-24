import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  port='3307',
  user="root",
  password="Admin@123",
   database="pythndb"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE pythndb")

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
  # print(x)

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
  # print(x)

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# val = [
  # ('Peter', 'Lowstreet 4'),
  # ('Amy', 'Apple st 652'),
  # ('Hannah', 'Mountain 21'),
  # ('Michael', 'Valley 345'),
  # ('Sandy', 'Ocean blvd 2'),
  # ('Betty', 'Green Grass 1'),
  # ('Richard', 'Sky st 331'),
  # ('Susan', 'One way 98'),
  # ('Vicky', 'Yellow Garden 2'),
  # ('Ben', 'Park Lane 38'),
  # ('William', 'Central st 954'),
  # ('Chuck', 'Main Road 989'),
  # ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")

# print("1 record inserted, id:", mycursor.lastrowid)

mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
  # print(x)

myresult = mycursor.fetchone()

print(myresult)
