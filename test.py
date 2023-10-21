
from __future__ import print_function

hostname = 'localhost'
username = 'mypense3_surebetAdmin'
password = 'surebetadminpassword'
database = 'mypense3_sureBetDjangoDatabase'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT fname, lname FROM employee" )

    for firstname, lastname in cur.fetchall() :
        print( firstname, lastname )


print( "Using mysqlclient (MySQLdb):" )
import MySQLdb
myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
#doQuery( myConnection )
myConnection.close()

print( "Using mysql.connector:" )

'''
import mysql.connector
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print( "Using pymysql:" )
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()
'''
