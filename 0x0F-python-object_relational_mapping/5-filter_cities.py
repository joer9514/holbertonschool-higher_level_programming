#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in
the states table ofhbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    query_str = "SELECT cities.name FROM states \
                INNER JOIN cities ON cities.state_id = states.id \
                WHERE BINARY states.name = %s \
                ORDER BY cities.id ASC"
    cur.execute(query_str, (argv[4],))
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query_rows))
    cur.close()
    conn.close()
