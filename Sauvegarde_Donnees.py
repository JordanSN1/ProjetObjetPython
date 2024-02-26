import mysql.connector
import config
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
    def getutilisateur(self):
        """
        Cette fonction permet de récupérer l'utilisateur.
        :return:
        """
        self.cursor.execute(f"SELECT * FROM utilisateur")
        for element in self.cursor:
            return element
    def getIdRoles(self , role):

        """
        Cette fonction permet de récupérer l'id du rôle.
        :param role:
        :return:
        """
        self.cursor.execute(f"SELECT id_role FROM role WHERE role = '{role}'")
        for element in self.cursor:
            return element[0]
    def getLoginUtilisateur(self):
        """
        Cette fonction permet de récupérer le login de l'utilisateur.

        :return:
        """
        self.cursor.execute(f"SELECT login_utilisateur FROM utilisateur ")
        for element in self.cursor:
            return element

    def getIdUtilisateur(self, nom, prenom):
        """
        Cette fonction permet de récupérer l'id de l'utilisateur.
        :param nom:
        :param prenom:
        :return:
        """
        self.cursor.execute(f"SELECT id_utilisateur FROM utilisateur WHERE nom_utilisateur = '{nom}' AND prenom_utilisateur = '{prenom}'")
        for element in self.cursor:
            return element[0]

    def EnvoiDonneesUtilisateur(self, nom, prenom,login ,email, numTel, ville, id_projet, passwordHash, date_debut, id_role):
        """
        Cette fonction permet d'envoyer les données de l'utilisateur.
        :param nom:
        :param prenom:
        :param login:
        :param email:
        :param numTel:
        :param ville:
        :param id_projet:
        :param passwordHash:
        :param date_debut:
        :param id_role:
        :return:
        """
        requete = (f"INSERT INTO utilisateur (nom_utilisateur, prenom_utilisateur,login_utilisateur, email_utilisateur, numtel_utilisateur, ville_utilisateur, id_projet, password_hash, date_debut, id_role) VALUES ('{nom}','{prenom}','{login}','{email}','{numTel}','{ville}','{id_projet}','{passwordHash}','{date_debut}','{id_role}')")
        self.cursor.execute(requete)
        self.connection.commit()


    def EnvoiDonneesAppartientUnite(self, id_utilisateur, id_unite):
        """
        Cette fonction permet d'envoyer les données de l'appartenance de l'utilisateur à une unité.
        :param id_utilisateur:
        :param id_unite:
        :return:
        """
        requete = (f"INSERT INTO appartient (id_utilisateur, id_unite) VALUES ('{id_utilisateur}','{id_unite}')")
        self.cursor.execute(requete)
        self.connection.commit()

    def AjoutProjet(self, nom_projet, date_debut, date_fin):
        """
        Cette fonction permet d'ajouter un projet.
        :param nom_projet:
        :param date_debut:
        :param date_fin:
        :return:
        """
        requete = (f"INSERT INTO `projet`(`nom_projet`, `date_debut`, `date_fin`) VALUES ('{nom_projet}','{date_debut}','{date_fin}')")
        self.cursor.execute(requete)
        self.connection.commit()

    def AjoutUnite(self, nom_unite, region):
        """
        Cette fonction permet d'ajouter une unité.
        :param nom_unite:
        :param region:
        :return:
        """
        requete = (f"INSERT INTO `unite`(`nom_unite`, `region`) VALUES ('{nom_unite}','{region}')")
        self.cursor.execute(requete)
        self.connection.commit()


    def getIdUnite(self, nom_unite):
        """
        Cette fonction permet de récupérer l'id de l'unité.
        :param nom_unite:
        :return:
        """
        self.cursor.execute(f"SELECT id_unite FROM unite WHERE nom_unite = '{nom_unite}'")
        for element in self.cursor:
            return element[0]

    def getIdProjet(self,utilisateur):
        """
        Cette fonction permet de récupérer l'id du projet.
        :param utilisateur:
        :return:
        """
        self.cursor.execute(f"SELECT projet.nom_projet , projet.id_projet FROM projet INNER JOIN utilisateur ON projet.id_projet = utilisateur.id_projet WHERE nom_utilisateur = '{utilisateur}'")
        for element in self.cursor:
            return element
    def VerifierLogin(self, login):
        """
        Cette fonction permet de vérifier le login.
        :param login:
        :return:
        """
        self.cursor.execute(f"SELECT login_utilisateur FROM utilisateur WHERE login_utilisateur = '{login}'")
        for element in self.cursor:
            return element[0]
    def getHashPassword(self, login):
        """
        Cette fonction permet de récupérer le mot de passe hashé.
        :param login:
        :return:
        """
        self.cursor.execute(f"SELECT password_hash FROM utilisateur WHERE login_utilisateur = '{login}'")
        for element in self.cursor:
            return element[0]
    def afficherProjet(self):
        """
        Cette fonction permet d'afficher les projets.
        :return:
        """
        self.cursor.execute(f"SELECT * FROM projet")
        for element in self.cursor:
            return(element)
    def UpdateProjetUtilisateur(self, id_projet, id_utilisateur):
        """
        Cette fonction permet de mettre à jour le projet de l'utilisateur.
        :param id_projet:
        :param id_utilisateur:
        :return:
        """
        requete = (f"UPDATE utilisateur SET id_projet = '{id_projet}' WHERE id_utilisateur = '{id_utilisateur}'")
        self.cursor.execute(requete)
        self.connection.commit()

sauvegarde = SauvegardeDonnees()

