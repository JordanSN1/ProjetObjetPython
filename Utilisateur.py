import random
import string as st
import datetime
import hashlib

class Utilisateur(object):

    def __init__(self):
        self.nom = ""
        self.prenom = ""
        self.age = 0
        self.email  = ""
        self.numTel = 0
        self.role = ""
        self.code_projet = ""
        self.passwordHash = ""
        self.date_debut = ""
        self.ville = ""
        self.password = ""
        self.caracteres = ""
    def saisie_utilisateur(self):
        self.nom = input("Veuillez saisir votre nom: ")
        self.prenom = input("Veuillez saisir votre prénom: ")
        self.age = int(input("Veuillez saisir votre âge: "))
        self.email = input("Veuillez saisir votre email: ")
        self.numTel = int(input("Veuillez saisir votre numéro de téléphone: "))
        self.ville = input("Veuillez saisir votre ville: ")
        self.role = input("Veuillez saisir votre role: ")
        self.code_projet = input("Veuillez saisir le code du projet: ")
        self.date_debut = datetime.datetime(int(input("Veuillez saisir l'année de début: ")), int(input("Veuillez saisir le mois de début: ")), int(input("Veuillez saisir le jour de début: ")) )
    def GenererLogin(self):
        self.login = f"{self.nom}.{self.prenom[0]}"
        return self.login
    def GenererPassword(self):
        self.caracteres = st.punctuation+ st.ascii_letters+ st.digits
        while True:
            self.taille = int(input("Veuillez saisir la taille pour votre mot de passe (Min : 12 , Max : 25): "))
            if self.taille < 12:
                print("Le mot de passe doit contenir au moins 12 caractères")

            elif self.taille > 25:
                print("Le mot de passe doit contenir au plus 25 caractères")
            else:
                break
        while True:

            for i in range(self.taille):
                index = random.randint(0, 2)
                self.password += self.caracteres[random.randint(0, len(self.caracteres)) - 1]

            return self.password
    def HashPassword(self):
        print("Le mot de passe hasher est : ")
        pwdh= hashlib.sha256(self.password.encode("utf-8")).hexdigest()
        print(pwdh)


Nabil = Utilisateur()
Nabil.saisie_utilisateur()
print(Nabil.GenererLogin())
print(Nabil.GenererPassword())
print(Nabil.HashPassword())