'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
Using Peewee, create tasks.db. Define a Task model with:
    - id (AutoField)
    - description (TextField)
    - priority (IntegerField)
    - done (BooleanField) (with a default value of False)
    
Insert three tasks and print all rows.
'''
from peewee import *

db = SqliteDatabase("tasks.db")
class Task(Model):
    id = AutoField()
    description = TextField()
    priority = IntegerField()
    done = BooleanField(default = False)

    class Meta:
        database = db
db.connect()
db.create_tables([Task])

task_1 = Task.create(description = "Fold all of the laundry and put it away", priority = 2)
task_2 = Task.create(description = "Wash and put away dishes", priority = 1)
task_3 = Task.create(description = "Do IS homework", priority = 3)

for task in Task.select():
    print(task.__data__)
