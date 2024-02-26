import mysql.connector
import config
class SauvegardeDonnees:
    def __init__(self):
        self.connection = mysql.connector.connect(user=config.DBConfig['user'],
                                                  password=config.DBConfig['password'],
                                                  host=config.DBConfig['host'],
                                                  database=config.DBConfig['database'])
        self.cursor = self.connection.cursor()
    def getIdRoles(self , role):
        self.cursor.execute(f"SELECT id_role FROM role WHERE role = '{role}'")
        for element in self.cursor:
            return element[0]
    def getIdUtilisateur(self, nom, prenom):
        self.cursor.execute(f"SELECT id_utilisateur FROM utilisateur WHERE nom_utilisateur = '{nom}' AND prenom_utilisateur = '{prenom}'")
        for element in self.cursor:
            return element[0]

    def EnvoiDonneesUtilisateur(self, nom, prenom, email, numTel, ville, id_projet, passwordHash, date_debut, id_role):
        requete = (f"INSERT INTO utilisateur (nom_utilisateur, prenom_utilisateur, email_utilisateur, numtel_utilisateur, ville_utilisateur, id_projet, password_hash, date_debut, id_role) VALUES ('{nom}','{prenom}','{email}','{numTel}','{ville}','{id_projet}','{passwordHash}','{date_debut}','{id_role}')")
        self.cursor.execute(requete)
        self.connection.commit()


    def EnvoiDonneesAppartientUnite(self, id_utilisateur, id_unite):
        requete = (f"INSERT INTO appartient (id_utilisateur, id_unite) VALUES ('{id_utilisateur}','{id_unite}')")
        self.cursor.execute(requete)
        self.connection.commit()

    def AjoutProjet(self, nom_projet, date_debut, date_fin):
        requete = (f"INSERT INTO `projet`(`nom_projet`, `date_debut`, `date_fin`) VALUES ('{nom_projet}','{date_debut}','{date_fin}')")
        self.cursor.execute(requete)
        self.connection.commit()

    def AjoutUnite(self, nom_unite, region):
        requete = (f"INSERT INTO `unite`(`nom_unite`, `region`) VALUES ('{nom_unite}','{region}')")
        self.cursor.execute(requete)
        self.connection.commit()


    def getIdUnite(self, nom_unite):
        self.cursor.execute(f"SELECT id_unite FROM unite WHERE nom_unite = '{nom_unite}'")
        for element in self.cursor:
            return element[0]

    def getIdProjet(self,utilisateur):
        self.cursor.execute(f"SELECT projet.nom_projet , projet.id_projet FROM projet INNER JOIN utilisateur ON projet.id_projet = utilisateur.id_projet WHERE nom_utilisateur = '{utilisateur}'")
        for element in self.cursor:
            return element
    def afficherProjet(self):
        self.cursor.execute(f"SELECT * FROM projet")
        for element in self.cursor:
            return(element)
    def UpdateProjetUtilisateur(self, id_projet, id_utilisateur):
        requete = (f"UPDATE utilisateur SET id_projet = '{id_projet}' WHERE id_utilisateur = '{id_utilisateur}'")
        self.cursor.execute(requete)
        self.connection.commit()

