#!/usr/bin/python3
"""
Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    query_str = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(query_str, (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
