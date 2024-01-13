#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
     # Create a cursor object to execute SQL queries
    cur = db.cursor()
    # Execute the SQL query
    cur.execute("SELECT * FROM states")
    # Fetch all rows
    rows = cur.fetchall()
    # Print the results
    for row in rows:
        print(row)
    # Close cursor and database connection
    cur.close()
    db.close()
