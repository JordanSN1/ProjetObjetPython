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
                    nom = utilisateur.set_nom(input("Entrez votre nom : ").upper())
                    prenom = utilisateur.set_prenom(input("Entrez votre prénom : ").upper())
                    loginBDD = sauvegarde.getAllLogin()
                    data = []
                    for element in loginBDD:
                        if element != '':
                            data.append(element)
                    if utilisateur.GenererLogin()  in data:
                        print("Ce login existe déjà.")
                    else :
                        utilisateur.GenererLogin()



                    print(f"Voici votre login, ne le perdez pas ! : {utilisateur.GenererLogin()}")
                    print(f"Voici votre mot de passe, ne le perdez pas ! : {utilisateur.GenererPassword()}")
                    utilisateur.HashPassword()
                    utilisateur.set_email(input("Entrez votre email : "))
                    utilisateur.set_numTel(input("Entrez votre numéro de téléphone : "))
                    utilisateur.set_ville(input("Entrez votre ville : "))
                    while True:
                        role = input(
                            "Entrez votre role [chercheur scientifique,collaborateur médecin,collaborateur commercial,assistant] : ")

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
                    nomutilisateurSupp = input("Entrez le nom de l'utilisateur à supprimer : ")
                    prenomutilisateurSupp = input("Entrez le prénom de l'utilisateur à supprimer : ")
                    idUtilisateurSupp = sauvegarde.getIdUtilisateur(nomutilisateurSupp, prenomutilisateurSupp)
                    try:
                        sauvegarde.supprimerUtilisateur(idUtilisateurSupp)
                    except Exception as e:
                        print(f"Erreur : {e}")

                    print(f"L'utilisateur {nomutilisateurSupp,prenomutilisateurSupp} a été supprimé.")
                elif choix == 3 :
                    choixDel = int(input("1. Modifier le nom\n2. Modifier le prénom\n3. Modifier le numéro de téléphone\n4. Modifier la ville\n5. Modifier le mot de passe\n6. Quittez\nEntrez votre choix:"))
                    if choixDel == 1:
                        nom = input("Entrez le nom de l'utilisateur à modifier : ")
                        newNom = input("Entrez le nouveau nom : ")
                        try:
                            sauvegarde.UpdateNomUtilisateur(nom, newNom)
                        except Exception as e:
                            print(f"Erreur : {e}")
                    elif choixDel == 2:
                        prenom = input("Entrez le prénom de l'utilisateur à modifier : ")
                        newPrenom = input("Entrez le nouveau prénom : ")
                        try:
                            sauvegarde.UpdatePrenomUtilisateur(prenom, newPrenom)
                        except Exception as e:
                            print(f"Erreur : {e}")
                    elif choixDel == 3:
                        numTel = input("Entrez le numéro de téléphone de l'utilisateur à modifier : ")
                        newNumTel = input("Entrez le nouveau numéro de téléphone : ")
                        try:
                            sauvegarde.UpdateNumTelUtilisateur(numTel, newNumTel)
                        except Exception as e:
                            print(f"Erreur : {e}")
                    elif choixDel == 4:
                        ville = input("Entrez la ville de l'utilisateur à modifier : ")
                        newVille = input("Entrez la nouvelle ville : ")
                        try:
                            sauvegarde.UpdateVilleUtilisateur(ville, newVille)
                        except Exception as e:
                            print(f"Erreur : {e}")
                    elif choixDel == 5:
                        UtilisateurNom = input("Entre le nom de l'utilisateur a changer le mot de passe : ")
                        UtilisateurPrenom = input("Entre le prenom de l'utilisateur a changer le mot de passe : ")
                        NewPassword = input("Entrez le nouveau mot de passe : ")
                        id_utilisateur = sauvegarde.getIdUtilisateur(UtilisateurNom, UtilisateurPrenom)
                        try:
                            sauvegarde.UpdatePasswordUtilisateur(NewPassword, id_utilisateur)
                        except Exception as e:
                            print(f"Erreur : {e}")
                    elif choixDel == 6:
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
