import sqlite3

## Connect to SQLite database
connection=sqlite3.connect("test.db")

# Create a curser object to insert records or create a table
# It is responsible for traversing the entire table (insert, retrieve)
cursor=connection.cursor()

table_info="""CREATE TABLE STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));"""
cursor.execute(table_info)
# Insert records
cursor.execute('''INSERT INTO STUDENT VALUES('Himaja','ComputerScience','A')''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sandeep','MBA','B')''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sukesh','CA','A')''')
cursor.execute('''INSERT INTO STUDENT VALUES('Teja','DataScience','B')''')
cursor.execute('''INSERT INTO STUDENT VALUES('Praveen','DataScience','B')''')

# Dispaly all the records
print("The inserted records are ")
data=cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()

