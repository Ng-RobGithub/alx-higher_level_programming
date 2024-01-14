#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    """ Connect to MySQL server """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    """ Create a cursor object to interact with the database """
    cur = db.cursor()
    """ Execute the query to get all cities """
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    """ Fetch all the rows """
    rows = cur.fetchall()
    """ Display the results """
    for row in rows:
        print(row)
    """ Close cursor and database connection """
    cur.close()
    db.close()
