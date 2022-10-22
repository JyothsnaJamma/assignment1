import sqlite3

conn=sqlite3.connect('Tutorial.db')
c=conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS company(Employee TEXT, Department TEXT, project TEXT)')
	
def data_entry(Employee, Department,Project):
	c.execute('INSERT INTO company VALUES(?, ?, ?)',(Employee, Department,Project))
	conn.commit()
	
Employee=input('Employee: ')
Department=input('Department: ')
Project=input('Project: ')

data_entry(Employee, Department,Project)

c.close()
conn.close()
