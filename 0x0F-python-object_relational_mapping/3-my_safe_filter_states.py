#!/usr/bin/python3
"""Lists all States with names starts with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (searched,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
