import mysql.connector
import config

connection = mysql.connector.connect(user=config.DBConfig['user'], password=config.DBConfig['password'],
                                     host=config.DBConfig['host'], database='sntlabo')

cursor = connection.cursor()

try:
    cursor.execute("SELECT * FROM utilisateur")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    if not rows:
        print("Aucun résultat")
finally:
    cursor.close()
    connection.close()
