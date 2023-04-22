#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa

 """

import MySQLdb
import sys

if __name__ == "__main__":
    """
     Connect to the MySQL database using the provided credentials
    """
    db = MySQLdb.connect(user= sys.argv[1], passwd= sys.argv[2], db= sys.argv[3])
    cur = db.cursor()
    
    query="SELECT c.id, c.name, s.name FROM cities as c\
                        inner join states as s\
                        ON c.state_id = s.id"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
