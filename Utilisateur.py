class Utilisateur(object):
    def afficher_menu(self):
        print("Menu:")
        print("1. Saisir nom et prénom")
        print("2. Saisir age")
        print("3. Affichage")
        print("4. Quitter")
        print("5. Login")

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def saisir_nom_prenom(self):
        self.nom = input("Entrez votre nom : ")
        confirmation_nom = input("Taper Oui si votre nom est correct pour continuer sinon taper Non ").upper()
        if confirmation_nom != "OUI":
            self.nom = input("Entrez votre nom correctement, vous pouvez le changer qu'une seule fois : ")

        self.prenom = input("Entrez votre prénom : ")
        confirmation_prenom = input("Taper Oui si votre prénom est correct pour continuer sinon taper Non ").upper()
        if confirmation_prenom != "OUI":
            self.prenom = input("Entrez votre prénom correctement, vous pouvez le changer qu'une seule fois : ")

    def saisir_age(self):
        self.age = input("Entrez votre âge : ")
        while not self.age.isdigit():
            print("L'âge doit être un nombre. Veuillez entrer votre âge correctement.")
            self.age = input("Entrez votre âge : ")
        self.age = int(self.age)  # Convertir l'âge en entier après validation

    def affichage(self):
        print("Vos informations :")
        print(f"Votre Nom : {self.nom}\nVotre Prénom : {self.prenom}\nVotre Âge : {self.age}")

Nabil = Utilisateur(nom='', prenom='', age=0)
while True:
    Nabil.afficher_menu()
    choix = input("Choisissez une option (1, 2, 3, 4, 5) : ")
    if choix == '1':
        Nabil.saisir_nom_prenom()
    elif choix == '2':
        Nabil.saisir_age()
    elif choix == '3':
        Nabil.affichage()
    elif choix == '4':
        break
    else:
        print("Choix non valide. Veuillez sélectionner une option valide.")
