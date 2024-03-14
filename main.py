import Utilisateur as ut
import Sauvegarde_Donnees as sd
import hashlib
import getpass
'''
pour avoir une liste propre
sauv = SauvegardeDonnees()
loginBDD = sauv.getAllLogin()
data = []
for element in loginBDD :
    if element != '':
        data.append(element)
print(data)
'''
def main():
    Erreur = 0
    Connexion = bool
    Connexionadmin = bool

    utilisateur = ut.Utilisateur()
    sauvegarde = sd.SauvegardeDonnees()

    while True :
        print("Se connecter:")
        login = input("Entrez votre login :")
        if login == 'admin' :
            password = getpass.getpass("Entrez votre mot de passe: ")
            if hashlib.sha256(password.encode("utf-8")).hexdigest() == sauvegarde.getHashPassword(login):
                print("Vous êtes connecté en tant qu'administrateur.")
                Connexionadmin = True
            else:
                print("Mot de passe incorrect.")
                Erreur += 1
                if Erreur == 3:
                    print("Vous avez fait 3 erreurs.")
                    exit()
            while Connexionadmin :
                choix = int(input("\tMenu:\n1. Créer un utilisateur\n2. Supprimer un utilisateur\n3. Update un utilisateur\n4. Ajouter un projet\n5. Update l'uniter de l'utilisateur\n6. Quittez\nEntrez votre choix:"))
                if choix == 1:
                    nom = utilisateur.set_nom(input("Entrez votre nom : ").lower())
                    prenom = utilisateur.set_prenom(input("Entrez votre prénom : ").lower())
                    loginBDD = sauvegarde.getAllLogin()
                    data = []
                    for element in loginBDD:
                        if element != '':
                            data.append(element)


                    login = utilisateur.GenererLogin(data)



                    print(f"Voici votre login, ne le perdez pas ! : {login}")
                    print(f"Voici votre mot de passe, ne le perdez pas ! : {utilisateur.GenererPassword()}")
                    utilisateur.HashPassword()
                    utilisateur.set_email(input("Entrez votre email : "))
                    numTel = input("Entrez votre numéro de téléphone : ")
                    while numTel.isdigit() == False:
                        print("Entrez un numéro de téléphone valide.")
                    utilisateur.set_numTel(input("Entrez votre numéro de téléphone : "))


                    utilisateur.set_ville(input("Entrez votre ville : ").lower())
                    while True:
                        role = input(
                            "Entrez votre role [chercheur scientifique,collaborateur médecin,collaborateur commercial,assistant] : ").lower()

                        if role in sauvegarde.getRoles():
                            utilisateur.set_role(role)
                            break
                        else:
                            print("Ce role n'existe pas.")
                    utilisateur.set_code_projet(input("Entrez le code du projet : "))
                    utilisateur.set_date_debut(input("Entrez l'année de début : "),input("Entrez le mois de début : "),input("Entrez le jour de début : "))

                    id_role = sauvegarde.getIdRoles(utilisateur.get_role())
                    sauvegarde.EnvoiDonneesUtilisateur(utilisateur.get_nom(), utilisateur.get_prenom(),
                                                               utilisateur.get_login(), utilisateur.get_email(),
                                                               utilisateur.get_numTel(), utilisateur.get_ville(),
                                                               utilisateur.get_code_projet(),
                                                               utilisateur.get_passwordHash(),
                                                               utilisateur.get_date_debut(), id_role)

                elif choix == 2 :
                    loginUtilisateurSupp = input("Entrez le login à supprimer : ").lower()
                    try:
                        sauvegarde.supprimerUtilisateur(login)
                    except Exception as e:
                        print(f"Erreur : {e}")

                    print(f"L'utilisateur {loginUtilisateurSupp} a été supprimé.")
                elif choix == 3 :
                    ChoixModif = int(input("1. Modifier le nom\n2. Modifier le prénom\n3. Modifier le numéro de téléphone\n4. Modifier la ville\n5. Modifier le mot de passe\n6. Quittez\nEntrez votre choix:"))
                    if ChoixModif == 1:
                        login = input("Entrez le login de l'utilisateur à modifier : ")
                        newNom = input("Entrez le nouveau nom : ")
                        print(login, newNom)
                        try:
                            sauvegarde.UpdateNomUtilisateur(login, newNom)
                        except Exception as e:
                            print(f"Erreur : {e}")
                    elif ChoixModif == 2:
                        login = input("Entrez le login de l'utilisateur à modifier : ")
                        newPrenom = input("Entrez le nouveau prénom : ")
                        try:
                            sauvegarde.UpdatePrenomUtilisateur(login, newPrenom)
                        except Exception as e:
                            print(f"Erreur : {e}")
                    elif ChoixModif == 3:
                        login = input("Entrez le login de l'utilisateur à modifier : ")
                        newNumTel = input("Entrez le nouveau numéro de téléphone : ")
                        try:
                            sauvegarde.UpdateNumTelUtilisateur(login, newNumTel)
                        except Exception as e:
                            print(f"Erreur : {e}")
                    elif ChoixModif == 4:
                        login = input("Entrez le login de l'utilisateur à modifier : ")
                        newVille = input("Entrez la nouvelle ville : ")
                        try:
                            sauvegarde.UpdateVilleUtilisateur(login, newVille)
                        except Exception as e:
                            print(f"Erreur : {e}")
                    elif ChoixModif == 5:
                        login = input("Entrez le login de l'utilisateur à modifier : ")
                        NewPassword =  utilisateur.GenererPassword()
                        try:
                            sauvegarde.UpdatePasswordUtilisateur(login, NewPassword)
                        except Exception as e:
                            print(f"Erreur : {e}")
                    elif ChoixModif == 6:
                        break

                elif choix == 4:
                    nom_projet = input("Entrez le nom du projet : ")
                    date_debut = input("Entrez l'année de début : ")
                    date_fin = input("Entrez l'année de fin : ")
                    try:
                        sauvegarde.AjoutProjet(nom_projet, date_debut, date_fin)
                    except Exception as e:
                        print(f"Erreur : {e}")
                elif choix == 5:
                    nomUtilisateur = input("Entrez le nom de l'utilisateur : ")
                    NouvelleUnite = input("Entrez le nom de l'unite : ")
                    sauvegarde.UpdateUniteUtilisateur(NouvelleUnite, nomUtilisateur)
                elif choix == 6:
                    exit()




if __name__ == "__main__":
    main()


























