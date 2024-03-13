import Utilisateur as ut
import Sauvegarde_Donnees as sd
import hashlib
import getpass

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
                if Connexionadmin :
                    choix = int(input("\tMenu:\n1. Créer un utilisateur\n2. Supprimer un utilisateur\n3. Update un utilisateur\n4. Ajouter un projet\n5. Update l'uniter de l'utilisateur\n6. Quittez\nEntrez votre choix:"))
                    print(choix)
                    if choix == 1:
                        utilisateur.saisie_utilisateur()
                        print(f"Voici votre login, ne le perdez pas ! : {utilisateur.GenererLogin()}")
                        print(f"Voici votre mot de passe, ne le perdez pas ! : {utilisateur.GenererPassword()}")
                        utilisateur.HashPassword()
                        id_role = sauvegarde.getIdRoles(utilisateur.get_role())

                        id_utilisateur = sauvegarde.getIdUtilisateur(utilisateur.get_nom(), utilisateur.get_prenom())
                        if id_utilisateur is not None:
                            if sauvegarde.getLoginUtilisateur(id_utilisateur) == []:
                                print("Ce login existe déjà.")
                        else:
                            sauvegarde.EnvoiDonneesUtilisateur(utilisateur.get_nom(), utilisateur.get_prenom(),
                                                               utilisateur.get_login(), utilisateur.get_email(),
                                                               utilisateur.get_numTel(), utilisateur.get_ville(),
                                                               utilisateur.get_code_projet(),
                                                               utilisateur.get_passwordHash(),
                                                               utilisateur.get_date_debut(), id_role)

                    elif choix == 2 :
                        utilisateurSupp = input("Entrez le nom de l'utilisateur à supprimer : ")

                        idUtilisateurSupp = sauvegarde.getIdUtilisateur(utilisateurSupp)
                        try:
                            sauvegarde.SupprimerUtilisateur(idUtilisateurSupp)
                        except Exception as e:
                            print(f"Erreur : {e}")

                        print(f"L'utilisateur {utilisateurSupp} a été supprimé.")
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
                            UpdatePassword = input("Entre le nom de l'utilisateur a changer le mot de passe : ")
                            NewPassword = input("Entrez le nouveau mot de passe : ")
                            id_utilisateur = sauvegarde.getIdUtilisateur(UpdatePassword)
                            try:
                                sauvegarde.UpdatePasswordUtilisateur(NewPassword, id_utilisateur)
                            except Exception as e:
                                print(f"Erreur : {e}")
                        elif choixDel == 6:
                            break



                    elif choix == 6:
                        break

            else:
                print("Mot de passe incorrect.")
                Erreur += 1
                if Erreur == 3:
                    print("Vous avez fait trop d'erreurs.")
                    break


if __name__ == "__main__":
    main()
