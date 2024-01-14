#!/usr/bin/python3
""" lists all cities of a given state from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    """ Connect to MySQL server """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    """ Create a cursor object to interact with the database """
    cur = db.cursor()
    """ Execute the query to get cities of the given state """
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    """ Fetch all the rows """
    rows = cur.fetchall()
    """ Display the results """
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    """ Close cursor and database connection """
    cur.close()
    db.close()
