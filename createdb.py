import sqlite3

conn = sqlite3.connect('agricultureuser.db')
print("Opened database successfully")

conn.execute('CREATE TABLE agriuser(name VARCHAR(20)not null, phono VARCHAR(10) not null, email VARCHAR(50) not null,username VARCHAR(20) not null,password VARCHAR(20) not null)')
print("Table created successfully")
conn.close()