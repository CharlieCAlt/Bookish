import sqlite3
from sqlite3 import Error
#import pandas as pd

# Create the sqlite database if it does not exist. If it exist, connect to it.
try:
  conn = sqlite3.connect('database.db')
except Error as e:
  print(e)

# Create a cursor to allow to execute SQL commands
cursor = conn.cursor()

# Create a SQL Table
sql_command = '''
    CREATE TABLE IF NOT EXISTS contacts (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Firstname TEXT, 
        Lastname TEXT, 
        Email TEXT
    )'''

cursor.execute(sql_command)

insert_data = f"""
    INSERT INTO contacts 
    (Firstname, Lastname, Email) 
    VALUES (
        'David',
        'Attenborough',
        'dattenborough@example.com'
    )
"""
cursor.execute(insert_data)
# Commit the changes to the database
conn.commit()

select_data = 'SELECT * FROM contacts'
cursor.execute(select_data)

rows = cursor.fetchall()

for row in rows:
  print(row)

users = [
  {'Firstname': 'Jane', 'Lastname': 'Goodall', 'Email': 'jgoodall@example.com'},
  {'Firstname': 'Rachel', 'Lastname': 'Carson', 'Email': 'rcarson@example.com'},
  {'Firstname': 'Barry', 'Lastname': 'Bishop', 'Email': 'bbishop@example.com'},
  {'Firstname': 'Edward', 'Lastname': 'J.Laurent', 'Email': 'ejlaurent@example.com'}
]

for user in users:
  insert_data = f"""
    INSERT INTO contacts 
    (Firstname, Lastname, Email) 
    VALUES (
        '{user['Firstname']}',
        '{user['Lastname']}',
        '{user['Email']}'
    )
    """
  cursor.execute(insert_data)
  conn.commit()

#
# df = pd.read_sql_query(select_data, conn)
# df
# # Close the Database
conn.close()