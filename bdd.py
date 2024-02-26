import mysql.connector
import config

connection = mysql.connector.connect(user=config.DBConfig['user'], password=config.DBConfig['password'],
                                     host=config.DBConfig['host'], database='sntlabo')

cursor = connection.cursor()
