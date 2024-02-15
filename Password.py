import string as st
import random


class Password:
    def __init__(self, password=""):
        self.password = password
        self.caracteres = [st.punctuation, st.ascii_letters, st.digits]
        self.taille = 0

    def generer_mdp(self):
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
                self.password += self.caracteres[index][random.randint(0, len(self.caracteres[index])) - 1]

            return self.password


nabil = Password()
print(nabil.generer_mdp())
