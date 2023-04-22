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

if __name__ == "__main__":
    """
     Connect to the MySQL database using the provided credentials
    """
    query="SELECT * FROM states WHERE BINARY name LIKE %s ORDER BY states.id ASC"
    cur.execute(query,(sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
