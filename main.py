import Utilisateur as ut
import Sauvegarde_Donnees as sd

def main():
    utilisateur = ut.Utilisateur()
    sauvegarde = sd.SauvegardeDonnees()
    if sauvegarde.afficherProjet() == []:
        print("Aucun projet n'a été ajouté.")
        nom_projet = input("Entrez le nom du projet: ")
        date_debut = input("Entrez la date de début du projet (YYYY-MM-DD): ")
        date_fin = input("Entrez la date de fin du projet (YYYY-MM-DD): ")
        sauvegarde.AjoutProjet(nom_projet, date_debut, date_fin)



    while True:
        print("\n1. Ajouter un utilisateur")
        print("2. Ajouter un projet")
        print("3. Quitter")

        choice = input("\nChoisissez une option: ")

        if choice == '1':
            utilisateur.saisie_utilisateur()
            utilisateur.GenererLogin()
            utilisateur.GenererPassword()
            utilisateur.HashPassword()
            id_role = sauvegarde.getIdRoles(utilisateur.get_role())
            sauvegarde.EnvoiDonneesUtilisateur(utilisateur.get_nom(), utilisateur.get_prenom(), utilisateur.get_email(),
                                               utilisateur.get_numTel(), utilisateur.get_ville(), utilisateur.get_code_projet(),
                                               utilisateur.get_passwordHash(), utilisateur.get_date_debut(), id_role)
        elif choice == '2':
            nom_projet = input("Entrez le nom du projet: ")
            date_debut = input("Entrez la date de début du projet (YYYY-MM-DD): ")
            date_fin = input("Entrez la date de fin du projet (YYYY-MM-DD): ")
            sauvegarde.AjoutProjet(nom_projet, date_debut, date_fin)
        elif choice == '3':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == '__main__':
    main()