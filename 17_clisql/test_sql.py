# Flying Turtles | Nicholas Tarsis, Anson Wong
# SoftDev
# K17 -- Starting sqlite3 Shell Basics
# 2022-10-25
#time spent: 0.5

import sqlite3 #enable SQLite operations

# open db if exists, otherwise create
db = sqlite3.connect("foo") #connection to database foo

# needed to execute statements & fetch results from queries
c = db.cursor() #facilitate db ops

# adds a table to database by executing "CREATE TABLE <name> (<col name> <data type>)" "
#will result in sqlite3.OperationalError: table roster already exists if run more than once
#c.execute("CREATE TABLE roster(name TEXT, userid INTEGER)")
#c.execute("CREATE TABLE ros(name TEXT, userid INTEGER)")

tables = c.execute("SELECT name FROM sqlite_master")
print("Tables")
print(tables.fetchall()) #returns a list of all table names from master

# adds a record to a table matching columns in order c.execute("""INSERT INTO <table name> VALUES(<value0>, <value1>,...)""");
c.execute("""INSERT INTO roster VALUES("frist", 19) """);
c.execute("""INSERT INTO roster VALUES("frista", 24) """);
c.execute("""INSERT INTO roster VALUES("fristb", 9) """);
#for i in range(20):
#    print(i)
#    c.execute("""INSERT INTO roster VALUES(str(i), i)""");

names = c.execute("SELECT name from roster")
userids = c.execute("SELECT userid from roster")
print("Names")
print(names.fetchall())
print("Userids")
print(userids.fetchall())

c.execute("DELETE FROM roster")
names = c.execute("SELECT name from roster")
userids = c.execute("SELECT userid from roster")
print("Names")
print(names.fetchall())
print("Userids")
#insertions need to be committed
db.commit() #save changes
db.close()