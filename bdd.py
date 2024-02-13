import mysql.connector
try:
    connection = mysql.connector.connect(user='root', password='', host='localhost', database='projetsntlabo')
    cursor = connection.cursor()
    print("Connexion à la base de données réussie")
except mysql.connector.Error:
    print("Connexion à la base de données échouée")