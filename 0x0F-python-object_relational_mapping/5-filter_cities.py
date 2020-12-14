#!/usr/bin/python3
""" Python Project """


import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ lists all the states from the database"""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM states, cities WHERE
                states.id = cities.state_id and states.name
                = %s ORDER BY cities.id ASC""", (argv[4],))
    content = cur.fetchall()
    disp = ""
    for i in content:
        disp = disp + i[0] + ", "
    print(disp[0:-2])
    cur.close()
    db.close()
