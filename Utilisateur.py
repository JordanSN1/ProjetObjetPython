import random
import string as st
import datetime
import hashlib

class Utilisateur(object):

    def __init__(self):
        self._nom = ""
        self._prenom = ""
        self._email = ""
        self._numTel = 0
        self._role = ""
        self._code_projet = ""
        self._passwordHash = ""
        self._date_debut = ""
        self._ville = ""
        self._password = ""
        self._caracteres = ""
        self._login = ""
    def set_nom(self, nom):
        self._nom = nom.split()
        self._nom = self._nom

    def set_prenom(self, prenom):
        self._prenom = prenom.split()


    def set_email(self, email):
        self._email = email.lower()

    def set_numTel(self, numTel):
        self._numTel = numTel

    def set_ville(self, ville):
        self._ville = ville.lower()

    def set_role(self, role):
        self._role = role.lower()

    def set_code_projet(self, code_projet):
        self._code_projet = code_projet

    def set_date_debut(self, annee , mois , jour):
        self._date_debut = '{0}-{1}-{2}'.format(annee, mois, jour)
    def GenererLogin(self, listeLogin):
        self._login = self._prenom[0][0] + '.' + self._nom[-1]
        if self._login.lower() in listeLogin:
            self._login = self._prenom[0][0] + '.' + self._nom[-1] + str(random.randint(1, 100))
        return self._login.lower()

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



