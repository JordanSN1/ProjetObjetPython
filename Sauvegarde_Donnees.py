import mysql.connector
import config
import hashlib



class SauvegardeDonnees:
    def __init__(self):

        """
        Cette fonction permet de se connecter à la base de données.
        """
        try:
            self.connection = mysql.connector.connect(user=config.DBConfig['user'],
                                                      password=config.DBConfig['password'],
                                                      host=config.DBConfig['host'],
                                                      database=config.DBConfig['database'])
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Erreur : {e}")

    # Les gets
    def getRoles(self):
        try:
            self.cursor.execute("SELECT role FROM role")
            result = self.cursor.fetchall()
            data = []
            for element in result:
                for el in element:
                    if el != '':
                        data.append(el)
            return data
        except Exception as e:
            print(f"Erreur : {e}")


        
    def getutilisateur(self):
        try:
            self.cursor.execute("SELECT * FROM utilisateur")
            result = self.cursor.fetchall()
            for element in result:
                return element
        except Exception as e:
            print("Une erreur est survenue lors de la récupération des utilisateurs :", e)
            return None

    def getIdRoles(self, role):
        try:
            self.cursor.execute(f"SELECT id_role FROM role WHERE role = '{role}'")
            result = self.cursor.fetchall()
            for element in result:
                return element[0]
        except Exception as e:
            print("Une erreur est survenue lors de la récupération de l'ID du rôle :", e)
            return None

    def getAllLogin(self):
        try:
            self.cursor.execute("SELECT login_utilisateur FROM utilisateur")
            result = self.cursor.fetchall()
            ListeLogin = []
            for element in result:
                for el in element:
                    if el != '':
                        ListeLogin.append(el)
            return ListeLogin
        except Exception as e:
            print("Une erreur est survenue lors de la récupération de tous les logins :", e)
            return []
    
    def getanciennete(self, login):
        try:
            requete = (f"SELECT YEAR(NOW()) - YEAR(utilisateur.date_debut) AS annees_ecoulees FROM utilisateur WHERE login_utilisateur = '{login}'")
            self.cursor.execute(requete)
            result = self.cursor.fetchall()
            for element in result:
                return element[0]
        except Exception as e:
            print("Une erreur est survenue lors de la récupération de l'ancienneté de l'utilisateur :", e)
            return None


    def getLoginUtilisateur(self, id_utilisateur):
        try:
            self.cursor.execute(f"SELECT login_utilisateur FROM utilisateur WHERE id_utilisateur = {id_utilisateur}")
            result = self.cursor.fetchall()
            for element in result:
                return element[0]
        except Exception as e:
            print("Une erreur est survenue lors de la récupération du login de l'utilisateur :", e)
            return None

    def getLoginUtilisateur(self, id_utilisateur):
        try:
            self.cursor.execute(f"SELECT login_utilisateur FROM utilisateur WHERE id_utilisateur = {id_utilisateur}")
            result = self.cursor.fetchall()
            for element in result:
                return element[0]
        except Exception as e:
            print("Une erreur est survenue lors de la récupération du login de l'utilisateur :", e)
            return None

    def getIdUtilisateur(self, nom, prenom):
        try:
            self.cursor.execute(f"SELECT id_utilisateur FROM utilisateur WHERE nom_utilisateur = '{nom}' AND prenom_utilisateur = '{prenom}'")
            result = self.cursor.fetchall()
            for element in result:
                return element[0]
        except Exception as e:
            print("Une erreur est survenue lors de la récupération de l'ID de l'utilisateur :", e)
            return None

    def getIdUnite(self, nom_unite):
        try:
            self.cursor.execute(f"SELECT id_unite FROM unite WHERE nom_unite = '{nom_unite}'")
            result = self.cursor.fetchall()
            for element in result:
                return element[0]
        except Exception as e:
            print("Une erreur est survenue lors de la récupération de l'ID de l'unité :", e)
            return None

    def getIdProjet(self, utilisateur):
        try:
            self.cursor.execute(
                f"SELECT projet.nom_projet , projet.id_projet FROM projet INNER JOIN utilisateur ON projet.id_projet = utilisateur.id_projet WHERE nom_utilisateur = '{utilisateur}'")
            result = self.cursor.fetchall()
            for element in result:
                return element
        except Exception as e:
            print("Une erreur est survenue lors de la récupération de l'ID du projet :", e)
            return None

    def VerifierLogin(self, login):
        try:
            self.cursor.execute(f"SELECT login_utilisateur FROM utilisateur WHERE login_utilisateur = '{login}'")
            result = self.cursor.fetchall()
            for element in result:
                return element[0]
        except Exception as e:
            print("Une erreur est survenue lors de la vérification du login :", e)
            return None

    def getHashPassword(self, login):
        try:
            self.cursor.execute(f"SELECT password_hash FROM utilisateur WHERE login_utilisateur = '{login}'")
            result = self.cursor.fetchall()
            for element in result:
                return element[0]
        except Exception as e:
            print("Une erreur est survenue lors de la récupération du mot de passe hashé :", e)
            return None

    def afficherProjet(self):
        try:
            self.cursor.execute("SELECT * FROM projet")
            result = self.cursor.fetchall()
            for element in result:
                return (element)
        except Exception as e:
            print("Une erreur est survenue lors de l'affichage des projets :", e)
            return None

    # Les envois
    def EnvoiDonneesUtilisateur(self, nom, prenom, login, email, numTel, ville, id_projet, passwordHash, date_debut,id_role,role_unite='NULL'):
        try:
            nom_str = ''.join(nom)
            prenom_str = ''.join(prenom)
            login_str = login
            requete = ("INSERT INTO utilisateur (nom_utilisateur, prenom_utilisateur,login_utilisateur, email_utilisateur, numtel_utilisateur, ville_utilisateur, id_projet, password_hash, date_debut, id_role,role_unite) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            valeurs = (nom_str, prenom_str, login_str, email, numTel, ville, id_projet, passwordHash, date_debut, id_role,role_unite)
            self.cursor.execute(requete,valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de l'envoi des données de l'utilisateur :", e)
    
    def EnvoiDonneesAppartientUnite(self, id_utilisateur, id_unite):
        try:
            requete = ("INSERT INTO appartient (id_utilisateur, id_unite) VALUES (%s,%s)")
            valeurs = (id_utilisateur, id_unite)
            self.cursor.execute(requete,valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de l'envoi des données d'appartenance à l'unité :", e)
    
    def EnvoiDonneesUnite(self, nom_unite, region):
        try:
            requete = ("INSERT INTO unite (nom_unite, region) VALUES (%s,%s)")
            valeurs = (nom_unite, region)
            self.cursor.execute(requete,valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de l'envoi des données de l'unité :", e)

    def AjoutProjet(self, nom_projet, date_debut, date_fin):
        try:
            requete = ("INSERT INTO `projet`(`nom_projet`, `date_debut`, `date_fin`) VALUES (%s,%s,%s)")
            valeurs = (nom_projet, date_debut, date_fin)
            self.cursor.execute(requete,valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de l'ajout d'un projet :", e)

    def AjoutUnite(self, nom_unite, region):
        try:
            requete = ("INSERT INTO `unite`(`nom_unite`, `region`) VALUES (%s,%s)")
            valeurs = (nom_unite, region)
            self.cursor.execute(requete,valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de l'ajout d'une unité :", e)

    # Les updates
    def UpdateProjetUtilisateur(self, id_projet, id_utilisateur):
        try:
            requete = "UPDATE utilisateur SET id_projet = %s WHERE id_utilisateur = %s"
            valeurs = (id_projet, id_utilisateur)
            self.cursor.execute(requete, valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de la mise à jour du projet de l'utilisateur :", e)

    def UpdateNomUtilisateur(self, login, NewName):
        try:
            requete = "UPDATE utilisateur SET nom_utilisateur = %s WHERE login_utilisateur = %s"
            valeurs = (NewName,login)
            self.cursor.execute(requete, valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de la mise à jour du nom de l'utilisateur :", e)

    def UpdatePrenomUtilisateur(self,login ,NewName):
        try:
            requete = ("UPDATE utilisateur SET prenom_utilisateur = %s WHERE login_utilisateur = %s")
            valeurs = (NewName, login)
            self.cursor.execute(requete, valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de la mise à jour du prénom de l'utilisateur :", e)

    def UpdateEmailUtilisateur(self,login ,NewEmail):
        try:
            requete = ("UPDATE utilisateur SET email_utilisateur = %s WHERE login_utilisateur = %s")
            valeurs = (NewEmail, login)
            self.cursor.execute(requete,valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de la mise à jour de l'email de l'utilisateur :", e)

    def UpdateNumTelUtilisateur(self,login ,NewNumTel):
        try:
            requete = ("UPDATE utilisateur SET numtel_utilisateur = %s WHERE login_utilisateur = %s")
            valeurs = (NewNumTel, login)
            self.cursor.execute(requete, valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de la mise à jour du numéro de téléphone de l'utilisateur :", e)

    def UpdateVilleUtilisateur(self,login ,NewVille):
        try:
            requete = ("UPDATE utilisateur SET ville_utilisateur = %s WHERE login_utilisateur = %s")
            valeurs = (NewVille, login)
            self.cursor.execute(requete,valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de la mise à jour de la ville de l'utilisateur :", e)

    def UpdatePasswordUtilisateur(self, login, NewPassword):
        try:
            NewPasswordhash = hashlib.sha256(NewPassword.encode("utf-8")).hexdigest()
            requete = ("UPDATE utilisateur SET password_hash = %s WHERE login_utilisateur = %s ")
            valeurs = (NewPasswordhash, (login,))  
            self.cursor.execute(requete, valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de la mise à jour du mot de passe de l'utilisateur :", e)

    def UpdateUniteUtilisateur(self, login, NewUnite):
        try:
            requete = ("UPDATE appartient SET id_unite = %s WHERE login_utilisateur = %s")
            valeurs = (NewUnite, login)
            self.cursor.execute(requete, valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de la mise à jour de l'unité de l'utilisateur :", e , "Veuillez vérifier que l'unité existe bien dans la base de données")

    def UpdateRoleUniteUtilisateur(self, login, NewRoleUnite):
        try:
            requete = ("UPDATE utilisateur SET role_unite = %s WHERE login_utilisateur = %s")
            valeurs = (NewRoleUnite, login)
            self.cursor.execute(requete, valeurs)
            self.connection.commit()
        except Exception as e:
            print("Une erreur est survenue lors de la mise à jour du rôle de l'unité de l'utilisateur :", e, "Veuillez vérifier que le rôle existe bien dans la base de données")
    

    # Les suppressions
    def supprimerUtilisateur(self, login):
        try:
            requete = ("DELETE FROM utilisateur WHERE login_utilisateur = %s")
            valeurs = (login,)  
            self.cursor.execute(requete, valeurs)
            self.connection.commit()
            print("Utilisateur supprimé")
        except Exception as e:
            print(f"Erreur : {e}")
        
    




