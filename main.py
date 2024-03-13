import Utilisateur as ut
import Sauvegarde_Donnees as sd
import hashlib


def main():
    Erreur = 0
    Connexion = bool

    utilisateur = ut.Utilisateur()
    sauvegarde = sd.SauvegardeDonnees()
    if sauvegarde.afficherProjet() is None:
        print("Aucun projet n'a été ajouté.")
        nom_projet = input("Entrez le nom du projet: ")
        date_debut = input("Entrez la date de début du projet (YYYY-MM-DD): ")
        date_fin = input("Entrez la date de fin du projet (YYYY-MM-DD): ")
        sauvegarde.AjoutProjet(nom_projet, date_debut, date_fin)

    while True:
        if sauvegarde.getutilisateur() is None:
            print("Aucun utilisateur n'a été ajouté.")
            print("Vous allez créer un premier utilisateur.")
            utilisateur.saisie_utilisateur()
            print(f"Voici votre login, ne le perdez pas ! : {utilisateur.GenererLogin()}")
            print(f"Voici votre mot de passe, ne le perdez pas ! : {utilisateur.GenererPassword()}")
            utilisateur.HashPassword()
            id_role = sauvegarde.getIdRoles(utilisateur.get_role())
            sauvegarde.EnvoiDonneesUtilisateur(utilisateur.get_nom(), utilisateur.get_prenom(), utilisateur.get_login(),
                                               utilisateur.get_email(), utilisateur.get_numTel(), utilisateur.get_ville(),
                                               utilisateur.get_code_projet(), utilisateur.get_passwordHash(),
                                               utilisateur.get_date_debut(), id_role)

        else:
            print("\nMenu:")
            print("1. Se connecter")
            print("2. Ajouter un utilisateur")
            print("3. Ajouter un projet")
            print("4. Quitter")

            choice = input("\nChoisissez une option: ")
            if choice == '1':
                while Erreur < 3:
                    login = input("Entrez votre login: ")
                    password = input("Entrez votre mot de passe: ")
                    if sauvegarde.VerifierLogin(login):
                        if hashlib.sha256(password.encode("utf-8")).hexdigest() == sauvegarde.getHashPassword(login):
                            print("Vous êtes connecté.")
                            Connexion = True
                            break
                        else:
                            print("Mot de passe incorrect.")
                            Erreur += 1
                else:
                    print("Tentatives de connexion dépassées. Veuillez réessayer plus tard.")
                    break
            elif choice == '2':
                if Connexion:
                    utilisateur.saisie_utilisateur()
                    print(f"Voici votre login, ne le perdez pas ! : {utilisateur.GenererLogin()}")
                    print(f"Voici votre mot de passe, ne le perdez pas ! : {utilisateur.GenererPassword()}")
                    utilisateur.HashPassword()
                    id_role = sauvegarde.getIdRoles(utilisateur.get_role())
                    sauvegarde.EnvoiDonneesUtilisateur(utilisateur.get_nom(), utilisateur.get_prenom(),
                                                       utilisateur.get_login(), utilisateur.get_email(),
                                                       utilisateur.get_numTel(), utilisateur.get_ville(),
                                                       utilisateur.get_code_projet(), utilisateur.get_passwordHash(),
                                                       utilisateur.get_date_debut(), id_role)
                else:
                    print("Vous devez être connecté pour ajouter un utilisateur.")
            elif choice == '3':
                if Connexion:
                    nom_projet = input("Entrez le nom du projet: ")
                    date_debut = input("Entrez la date de début du projet (YYYY-MM-DD): ")
                    date_fin = input("Entrez la date de fin du projet (YYYY-MM-DD): ")
                    sauvegarde.AjoutProjet(nom_projet, date_debut, date_fin)
                else:
                    print("Vous devez être connecté pour ajouter un projet.")
            elif choice == '4':
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

if __name__ == '__main__':
    main()
