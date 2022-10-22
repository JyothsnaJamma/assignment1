import sqlite3

conn=sqlite3.connect('Tutorial.db')
c=conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS people(name TEXT, age INTEGER, height REAL)')
	
def data_entry(name,age,height):
	c.execute('INSERT INTO people VALUES(?, ?, ?)',(name,age,height))
	conn.commit()
	
name=input('Name: ')
age=int(input('Age: '))
height=float(input('Height: '))

data_entry(name,age,height)

c.close()
conn.close()
