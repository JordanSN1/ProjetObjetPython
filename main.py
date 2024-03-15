import Utilisateur as ut
import Sauvegarde_Donnees as sd
import hashlib
import getpass
import time

def main():
    Erreur = 0
    Connexion = False
    Connexionadmin = False

    utilisateur = ut.Utilisateur()
    sauvegarde = sd.SauvegardeDonnees()

    while True :
        print("Se connecter:\n")
        login = input("Entrez votre login :")
        if login not in sauvegarde.getAllLogin():
            print("Ce login n'existe pas.\n")
            Erreur += 1
            if Erreur == 3:
                print("Vous avez fait 3 erreurs.\n")
                exit()
        
        if login == 'admin' :
            password = getpass.getpass("Entrez votre mot de passe: ")
            print("Nous vérifions votre identité. Veuillez patienter...\n")
            time.sleep(3)
            if hashlib.sha256(password.encode("utf-8")).hexdigest() == sauvegarde.getHashPassword(login):

                print("Vous êtes connecté en tant qu'administrateur.\n")
                Connexionadmin = True
                
            else:
                print("Mot de passe incorrect.\n")
                Erreur += 1
                if Erreur == 3:
                    print("Vous avez fait 3 erreurs.\n")
                    exit()
            while Connexionadmin :
                    choix = int(input("\tMenu:\n1. Créer un utilisateur\n2. Supprimer un utilisateur\n3. Update un utilisateur\n4. Ajouter un projet\n5. Update l'uniter de l'utilisateur\n6. Créer une uniter\n7. Passer un utilisateur en Chef\n8. Se deconnecter\n9. Quitter\n\nEntrez votre choix:"))
                    if choix == 1:
                        nom = utilisateur.set_nom(input("Entrez votre nom : ").lower())
                        prenom = utilisateur.set_prenom(input("Entrez votre prénom : ").lower())
                        loginBDD = sauvegarde.getAllLogin()
                        data = []
                        for element in loginBDD:
                            if element != '':
                                data.append(element)
                        ListeLogin = utilisateur.GenererLogin(data)



                        print(f"Voici votre login, ne le perdez pas ! : {ListeLogin}")
                        print(f"Voici votre mot de passe, ne le perdez pas ! : {utilisateur.GenererPassword()}")
                        utilisateur.HashPassword()
                        utilisateur.set_email(input("Entrez votre email : "))
                        numTel = input("Entrez votre numéro de téléphone : ")
                        while numTel.isdigit() == False:
                            print("Entrez un numéro de téléphone valide.")
                            numTel = input("Entrez votre numéro de téléphone : ")
                        utilisateur.set_numTel(numTel)


                        utilisateur.set_ville(input("Entrez votre ville : ").lower())
                        while True:
                            role = input("Entrez votre role [chercheur scientifique,collaborateur médecin,collaborateur commercial,assistant] : ").lower()
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
                        sauvegarde.supprimerUtilisateur(loginUtilisateurSupp)
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
                        loginUtilisateur = input("Entrez le login de l'utilisateur : ")
                        NouvelleUnite = input("Entrez le nom de l'unite : ")
                        sauvegarde.UpdateUniteUtilisateur(loginUtilisateur, NouvelleUnite)
                    
                    elif choix == 6:
                        NomUnite = input("Entrez le nom de l'unite : ")
                        region = input("Entrez la région : ")
                        try:
                            sauvegarde.AjoutUnite(NomUnite,region)
                        except Exception as e:
                            print(f"Erreur : {e}")

                    elif choix == 7:
                        loginUtilisateur = input("Entrez le login de l'utilisateur : ")
                        if sauvegarde.getanciennete(loginUtilisateur) >= 10:
                            sauvegarde.UpdateRoleUtilisateur(loginUtilisateur, "chef")
                            print("L'utilisateur est passé en chef.")
                        else:
                            print("L'utilisateur n'a pas l'ancienneté requise.")
                        
                    elif choix == 8:
                        print("Vous êtes déconnecté.")
                        Connexionadmin = False
                    elif choix == 9:
                        exit()




if __name__ == "__main__":
    main()


























