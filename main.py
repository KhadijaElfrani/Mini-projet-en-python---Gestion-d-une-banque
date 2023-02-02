from Client import Client
from Operation import Operation

if __name__ == "__main__":
    mon_client = Client()
    mon_operation = Operation()
    print("BIENVENUE DANS LA BANQUE")
    print("1.S'AUTHENTIFIER ")
    print("2.CREER MON COMPTE ")
    user = int(input("Votre choix ? "))

    if user == 1:
        print("--- S'AUTHENTIFIER ---")
        pseudo = input("Votre pseudo : ")
        telephone = int(input("Votre numero de telephone : "))
        mot_de_passe = input("Votre mot de passe : ")
        mon_client.sauthentifier(pseudo, telephone, mot_de_passe)
        while True:
            if mon_client.est_connecte:
                print("1.Ajouter montant ")
                print("2.Affiche solde ")
                print("3.Effectuer un virement ")
                print("4.Débiter montant")
                print("5.Afficher operations recentes")
                choix = int(input())
                if choix == 1:
                    mon_operation.affiche_solde(mon_client)
                    montant = int(input("Entrez le montant à ajouter "))
                    mon_operation.ajouter_solde(montant, mon_client)
                    mon_operation.affiche_solde(mon_client)
                    print("\n1.Revenir au Menu")
                    print("2.Déconnecter")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                if choix == 2:
                    mon_operation.affiche_solde(mon_client)
                    print("\n1.Revenir au Menu")
                    print("2.Déconnecter")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                if choix == 3:
                    montant = int(input("Entrez le montant à transferer : "))
                    pseudo_dest = input("Entrez le pseudo de votre destinataire : ")
                    telephone_dest = input("Entrez le numéro de téléphone de votre destinataire : ")
                    mon_operation.effectuer_virement(montant, pseudo_dest , telephone_dest , mon_client)
                    mon_operation.affiche_solde(mon_client)
                    print("\n1.Revenir au Menu")
                    print("2.Déconnecter")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                if choix == 4:
                    mon_operation.affiche_solde(mon_client)
                    montant = int(input("Entrez le montant à débiter "))
                    mon_operation.debiter_solde(montant, mon_client)
                    mon_operation.affiche_solde(mon_client)
                    print("\n1.Revenir au Menu")
                    print("2.Déconnecter")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                if choix == 5:
                    with open(f"{mon_client.pseudo}_releve.txt", "r") as f:
                        operations = f.read()
                        print(operations)
                    print("\n1.Revenir au Menu")
                    print("2.Déconnecter")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

    if user == 2:
        print("--- CREATION DU COMPTE ---")
        pseudo = input("Choisissez un pseudo : ")
        telephone = int(input("Votre numero de telephone : "))
        mot_de_passe = input("Choisissez votre mot de passe : ")
        solde_init = input("Entrez votre solde initial : ")
        mon_client.creer_compte(pseudo, telephone, solde_init, mot_de_passe)
