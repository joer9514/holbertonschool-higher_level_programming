#!/usr/bin/python3
""" Python Project """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ lists all the states from the database"""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY '{}' ORDER BY id ASC"""
                .format(argv[4]))
    content = cur.fetchall()
    for i in content:
        print("{}".format(i))
    cur.close()
    db.close()
