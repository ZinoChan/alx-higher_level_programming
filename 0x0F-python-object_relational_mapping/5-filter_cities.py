#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    cursor = db.cursor()

    cursor.execute(
        """SELECT cities.name FROM cities INNER JOIN states ON
        states.id=cities.state_id WHERE states.name=%s""",
        (state,),
    )
    rows = cursor.fetchall()
    city_name = list(row[0] for row in rows)
    print(*city_name, sep=", ")
    cursor.close()
    db.close()
