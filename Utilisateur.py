import random
import string as st
import datetime
import hashlib

class Utilisateur(object):

    def __init__(self):
        self._nom = str
        self._prenom = str
        self._email = str
        self._numTel = int
        self._role = str
        self._code_projet = str
        self._passwordHash = str
        self._date_debut = str
        self._ville = str
        self._password = str
        self._caracteres = str

    def saisie_utilisateur(self):
        self._nom = input("Veuillez saisir votre nom : ")
        self._prenom = input("Veuillez saisir votre prénom : ")
        self._email = input("Veuillez saisir votre email : ")
        self._numTel = int(input("Veuillez saisir votre numéro de téléphone : "))
        self._ville = input("Veuillez saisir votre ville : ")
        self._role = input("Veuillez saisir votre rôle : (chercheur scientifique, collaborateur médecin, collaborateur commercial, assistant)")
        self._code_projet = input("Veuillez saisir le code du projet : ")
        self._date_debut = datetime.datetime(int(input("Veuillez saisir l'année de début : ")),
                                              int(input("Veuillez saisir le mois de début : ")),
                                              int(input("Veuillez saisir le jour de début : ")))

    def GenererLogin(self):
        self._login = f"{self._nom}.{self._prenom[0]}"
        return self._login

    def GenererPassword(self):
        self._caracteres = st.punctuation + st.ascii_letters + st.digits
        while True:
            self._taille = int(input("Veuillez saisir la taille pour votre mot de passe (Min : 12, Max : 25): "))
            if self._taille < 12:
                print("Le mot de passe doit contenir au moins 12 caractères.")
            elif self._taille > 25:
                print("Le mot de passe doit contenir au plus 25 caractères.")
            else:
                break
        for i in range(self._taille):
            self._password += self._caracteres[random.randint(0, len(self._caracteres) - 1)]
        return self._password

    def HashPassword(self):
        self._passwordHash = hashlib.sha256(self._password.encode("utf-8")).hexdigest()
        return self._passwordHash

    # Getters
    def get_nom(self):
        return self._nom

    def get_prenom(self):
        return self._prenom
    
    def get_login(self):
        return self._login
    
    def get_email(self):
        return self._email

    def get_numTel(self):
        return self._numTel

    def get_role(self):
        return self._role

    def get_code_projet(self):
        return self._code_projet

    def get_passwordHash(self):
        return self._passwordHash

    def get_date_debut(self):
        return self._date_debut

    def get_ville(self):
        return self._ville

    def get_password(self):
        return self._password

    def get_caracteres(self):
        return self._caracteres

