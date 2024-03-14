import mysql.connector
import config
import hashlib

class SauvegardeDonnees:
    def __init__(self):

        """
        Cette fonction permet de se connecter à la base de données.
        """
        self.connection = mysql.connector.connect(user=config.DBConfig['user'],
                                                  password=config.DBConfig['password'],
                                                  host=config.DBConfig['host'],
                                                  database=config.DBConfig['database'])
        self.cursor = self.connection.cursor()

    # Les gets
    def getRoles(self):
        self.cursor.execute("SELECT role FROM role")
        result = self.cursor.fetchall()
        data = []
        for element in result:

            for el in element:
                if el != '':
                    data.append(el)
        return data

    def getutilisateur(self):
        self.cursor.execute(f"SELECT * FROM utilisateur")
        result = self.cursor.fetchall()
        for element in result:
            return element


    def getIdRoles(self, role):
        self.cursor.execute(f"SELECT id_role FROM role WHERE role = '{role}'")
        result = self.cursor.fetchall()
        for element in result:
            return element[0]


    def getAllLogin(self):
        self.cursor.execute(f"SELECT login_utilisateur FROM utilisateur")
        result = self.cursor.fetchall()
        for element in result:
            return element


    def getLoginUtilisateur(self, id_utilisateur):
        self.cursor.execute(f"SELECT login_utilisateur FROM utilisateur where id_utilisateur = {id_utilisateur}")
        result = self.cursor.fetchall()
        for element in result:
            return element[0]


    def getIdUtilisateur(self, nom, prenom):
        self.cursor.execute(
            f"SELECT id_utilisateur FROM utilisateur WHERE nom_utilisateur = '{nom}' AND prenom_utilisateur = '{prenom}'")
        result = self.cursor.fetchall()
        for element in result:
            return element[0]


    def getIdUnite(self, nom_unite):
        self.cursor.execute(f"SELECT id_unite FROM unite WHERE nom_unite = '{nom_unite}'")
        result = self.cursor.fetchall()
        for element in result:
            return element[0]


    def getIdProjet(self, utilisateur):
        self.cursor.execute(
            f"SELECT projet.nom_projet , projet.id_projet FROM projet INNER JOIN utilisateur ON projet.id_projet = utilisateur.id_projet WHERE nom_utilisateur = '{utilisateur}'")
        result = self.cursor.fetchall()
        for element in result:
            return element


    def VerifierLogin(self, login):
        self.cursor.execute(f"SELECT login_utilisateur FROM utilisateur WHERE login_utilisateur = '{login}'")
        result = self.cursor.fetchall()
        for element in result:
            return element[0]


    def getHashPassword(self, login):
        self.cursor.execute(f"SELECT password_hash FROM utilisateur WHERE login_utilisateur = '{login}'")
        result = self.cursor.fetchall()
        for element in result:
            return element[0]


    def afficherProjet(self):
        self.cursor.execute(f"SELECT * FROM projet")
        result = self.cursor.fetchall()
        for element in result:
            return (element)

    # Les envois
    def EnvoiDonneesUtilisateur(self, nom, prenom, login, email, numTel, ville, id_projet, passwordHash, date_debut,id_role):
        nom_str = ''.join(nom)
        prenom_str = ''.join(prenom)
        login_str = login
        requete = (f"INSERT INTO utilisateur (nom_utilisateur, prenom_utilisateur,login_utilisateur, email_utilisateur, numtel_utilisateur, ville_utilisateur, id_projet, password_hash, date_debut, id_role) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        valeurs = (nom_str, prenom_str, login_str, email, numTel, ville, id_projet, passwordHash, date_debut, id_role)
        self.cursor.execute(requete)
        self.connection.commit()

    def EnvoiDonneesAppartientUnite(self, id_utilisateur, id_unite):
        requete = (f"INSERT INTO appartient (id_utilisateur, id_unite) VALUES (%s,%s)")
        valeurs = (id_utilisateur, id_unite)
        self.cursor.execute(requete,valeurs)
        self.connection.commit()

    def AjoutProjet(self, nom_projet, date_debut, date_fin):
        requete = (f"INSERT INTO `projet`(`nom_projet`, `date_debut`, `date_fin`) VALUES (%s,%s,%s)")
        valeurs = (nom_projet, date_debut, date_fin)
        self.cursor.execute(requete,valeurs)
        self.connection.commit()

    def AjoutUnite(self, nom_unite, region):
        requete = (f"INSERT INTO `unite`(`nom_unite`, `region`) VALUES (%s,%s)")
        valeurs = (nom_unite, region)
        self.cursor.execute(requete,valeurs)
        self.connection.commit()

    # Les updates
    def UpdateProjetUtilisateur(self, id_projet, id_utilisateur):
        requete = "UPDATE utilisateur SET id_projet = %s WHERE id_utilisateur = %s"
        valeurs = (id_projet, id_utilisateur)
        self.cursor.execute(requete, valeurs)
        self.connection.commit()

    def UpdateNomUtilisateur(self, login, NewName):
        requete = "UPDATE utilisateur SET nom_utilisateur = %s WHERE login_utilisateur = %s"
        valeurs = (login, NewName)
        self.cursor.execute(requete, valeurs)
        self.connection.commit()

    def UpdatePrenomUtilisateur(self,login ,NewName):
        requete = (f"UPDATE utilisateur SET prenom_utilisateur = %s WHERE login_utilisateur = %s")
        valeurs = (login, NewName)
        self.cursor.execute(requete, valeurs)
        self.connection.commit()

    def UpdateEmailUtilisateur(self,login ,NewEmail):
        requete = (f"UPDATE utilisateur SET email_utilisateur = %s WHERE login_utilisateur = %s")
        valeurs = (login, NewEmail)
        self.cursor.execute(requete,valeurs)
        self.connection.commit()

    def UpdateNumTelUtilisateur(self,login ,NewNumTel):
        requete = (f"UPDATE utilisateur SET numtel_utilisateur = %s WHERE login_utilisateur = %s")
        valeurs = (login, NewNumTel)
        self.cursor.execute(requete, valeurs)
        self.connection.commit()

    def UpdateVilleUtilisateur(self,login ,NewVille):
        requete = (f"UPDATE utilisateur SET ville_utilisateur = %s WHERE login_utilisateur = %s")
        valeurs = (login, NewVille)
        self.cursor.execute(requete,valeurs)
        self.connection.commit()

    def UpdatePasswordUtilisateur(self,login ,NewPassword):
        NewPasswordhash = hashlib.sha256(NewPassword.encode("utf-8")).hexdigest()
        requete = (f"UPDATE utilisateur SET password_hash = %s WHERE login_utilisateur = %s ")
        valeurs = (NewPasswordhash, login)
        self.cursor.execute(requete,valeurs)
        self.connection.commit()

    def UpdateUniteUtilisateur(self ,login, NewUnite):
        requete = (f"UPDATE appartient SET id_unite = %s WHERE login_utilisateur = %s")
        valeurs = (NewUnite, login)
        self.cursor.execute(requete, valeurs)
        self.connection.commit()

    # Les suppressions
    def supprimerUtilisateur(self, login):
        requete = (f"DELETE FROM utilisateur WHERE login_utilisateur = %s")
        valeur = login
        self.cursor.execute(requete, valeur)
        self.connection.commit()

sauv = SauvegardeDonnees()
print(sauv.getRoles())

