import sqlite3

connection = sqlite3.connect('mydata.db')

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id_number INTEGER,
    first_name TEXT,
    last_name TEXT,
    age INTEGER)
""")

cursor.execute("""
INSERT INTO persons VALUES
(1, "Paul", "Smith", 24),
(2, "Mark", "Johnson", 42),
(3, "Anna", "Smith", 34)
""")

connection.commit()
connection.close()