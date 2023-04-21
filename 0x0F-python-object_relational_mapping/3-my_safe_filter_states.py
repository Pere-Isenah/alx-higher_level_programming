#!/usr/bin/python3
"""
 a script that takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument.
 But this time, write one that is safe from MySQL injections!

 """

import MySQLdb
import sys

db = MySQLdb.connect(user= sys.argv[1], passwd= sys.argv[2], db= sys.argv[3])
cur = db.cursor()

query="SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
cur.execute(query,(sys.argv[4],))
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
