from views import db
from models import Task
from datetime import date

#create the database and it's table
db.create_all()

#insert dummy data for testing. Commenting it out.
#db.session.add(Task("Finish this tutorial", date(2014, 3, 13),10, 1))

#db.session.add(Task("Finish Real Python", date(2014, 3, 13), 10 ,1))

#commit the insert
db.session.commit()

