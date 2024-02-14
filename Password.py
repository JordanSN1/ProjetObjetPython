import string as st
import random
class Password:
    def __init__(self, password = ""):
        self.password = password
        self.caracteres = [st.punctuation, st.ascii_letters, st.digits]

    def GenererMDP(self,taille = 0):
        while True :
            taille = int(input("Veuillez saisir la taille pour votre mot de passe (Min : 12 , Max : 45): "))
            if taille < 12:
                print("Le mot de passe doit contenir au moins 12 caractères")

            elif taille > 45:
                print("Le mot de passe doit contenir au plus 45 caractères")
            else:
                break
        while True:

            for i in range(taille):
                index = random.randint(0,2)
                self.password += self.caracteres[index][random.randint(0,len(self.caracteres[index]))-1]

            return self.password





nabil = Password()
print(nabil.GenererMDP())