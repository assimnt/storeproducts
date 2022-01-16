import datetime
import mysql.connector
__cnx = None
def get_serverconnection():
    if __cnx is None:
    cnx = mysql.connector.connect(user='root',password='SI03152398058',
                              host='127.0.0.1',
                               database='projectstore')
