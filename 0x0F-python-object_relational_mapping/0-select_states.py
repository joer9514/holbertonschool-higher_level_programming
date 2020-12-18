#!/usr/bin/python3
""" Python Project """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ lists all the states from the database"""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    content = cur.fetchall()
    for i in content:
        print(i)
    cur.close()
    db.close()
