#!/usr/bin/python3
"""
 a script that takes in the name of a state as an argument and lists all cities of that state, using the database
 """

import MySQLdb
import sys

if __name__ == "__main__":
    """
     Connect to the MySQL database using the provided credentials
    """
    db = MySQLdb.connect(user= sys.argv[1], passwd= sys.argv[2], db= sys.argv[3])
    cur = db.cursor()
    
    query="SELECT  c.name FROM cities as c\
                        inner join states as s\
                        ON c.state_id = s.id\
                        WHERE BINARY s.name = %s"
    
    cur.execute(query,(sys.argv[4],))
    rows = cur.fetchall()
    value_list=""
    for row in rows:
       value_list+= row[0] + ", "
    print(value_list[:-2])
    cur.close()
    db.close()
