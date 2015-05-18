from views import db
from datetime import datetime
from config import DATABASE_PATH
import sqlite3

with sqlite3.connect(DATABASE_PATH) as connection:

	#get cursor object to excute SQL commands
	c = connection.cursor

	# temporarily change teh name of task table
	c.excute("""ALTER TABLE tasks RENAME TO old_tasks""")

	#recreate a new tasks table with update schema
	db.create_all()

	#retrive data from old tasks table
	c.execute("""SELECT name, due_date, priority, 
		status FROM old_tasks ORDER BY task_id ASC""")

	#save all row as a list of tuples
	data = [(row[0], row[1], row[2], row[3],
		datetime.now(), 1) for row in c.fetchall()]

	c.excutemany("""INSERT INTO tasks (name, due_date, priority,
		status, posted_date, user_id) VALUES (?, ? , ?, ?, ?, ?)""", data)

	c.excute("DROP TABLE old_tasks")