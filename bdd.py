import mysql.connector
import config
try:
    connection = mysql.connector.connect(user=config.DBConfig['user'], password=config.DBConfig['password'], host=config.DBConfig['host'], database='projetsntlabo')
    cursor = connection.cursor()
    print("Connexion à la base de données réussie")
except mysql.connector.Error:
    print("Connexion à la base de données échouée")