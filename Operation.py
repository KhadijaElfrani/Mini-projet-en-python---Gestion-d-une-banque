import os
from datetime import datetime

class Operation:
    def __init__(self):
        self.liste_operations = []

    def pre_inserer_ligne(self, client_releve, ligne):
        """ Inserer la ligne en haut de fichier text """
        # definir un fichier temp
        temp_fichier = client_releve + '.bak'
        # ouvrir le fichier original en mode read et le fichier temp en mode write
        with open(client_releve, 'r') as read_obj, open(temp_fichier, 'w') as write_obj:
            write_obj.write(ligne + '\n')
            for ligne in read_obj:
                write_obj.write(ligne)
        os.remove(client_releve)
        os.rename(temp_fichier, client_releve)

    def ajouter_solde(self, montant, client, motif):
        conditions = True
        if montant <= 0:
            print("Montant invalide. ")
            conditions = False
        if conditions:
            client.solde += montant
            with open(f"{client.pseudo}.txt", "r") as f:
                details = f.read()
                client.client_details_list = details.split("\n")

            with open(f"{client.pseudo}.txt", "w") as f:
                f.write(details.replace(str(client.client_details_list[2]), str(client.solde)))

            print("Un montant de " + str(montant) + " a bien été ajoutée a votre solde  .")
            str1 = str(client.pseudo)+"_releve.txt"
            str2 = "Credit sous le motif : " + str(motif) + "    +" + str(montant)
            self.pre_inserer_ligne(str1, str2)

    def debiter_solde(self, montant, client, motif):
        conditions = True
        if montant <= 0:
            print("Montant invalide. ")
            conditions = False
        if conditions:
            client.solde -= montant
            with open(f"{client.pseudo}.txt", "r") as f:
                details = f.read()
                client.client_details_list = details.split("\n")

            with open(f"{client.pseudo}.txt", "w") as f:
                f.write(details.replace(str(client.client_details_list[2]), str(client.solde)))

            print("Un montant de " + str(montant) + " a bien été débité de votre solde  .")

            str1 = str(client.pseudo)+"_releve.txt"
            str2 = "Debit sous le motif : " + str(motif) + "    -" + str(montant)
            self.pre_inserer_ligne(str1, str2)

    def affiche_solde(self, client):
        print("Votre solde actuelle est de " + str(client.solde))

    def effectuer_virement(self, montant, pseudo, telephone, client):
        with open(f"{pseudo}.txt", "r") as f:
            details = f.read()
            client.client_details_list = details.split("\n")
            if str(telephone) in client.client_details_list:
                self.est_transfere = True

        if self.est_transfere == True:
            solde_dest = int(client.client_details_list[2]) + montant
            solde_client = client.solde - montant
            with open(f"{pseudo}.txt", "w") as f:
                f.write(details.replace(str(client.client_details_list[2]), str(solde_dest)))

            with open(f"{client.pseudo}.txt", "r") as f:
                details_2 = f.read()
                client.client_details_list = details_2.split("\n")

            with open(f"{client.pseudo}.txt", "w") as f:
                f.write(details_2.replace(str(client.client_details_list[2]), str(solde_client)))

            print("Amount Transfered Successfully to", pseudo, "-", telephone)
            client.solde = solde_client

            str1 = str(pseudo)+"_releve.txt"
            str2 = "Virement recu de la part de " + str(client.pseudo) + "     +" + str(montant)
            self.pre_inserer_ligne(str1, str2)
            str1 = str(client.pseudo)+"_releve.txt"
            str2 = "Virement envoye en faveur de " + str(pseudo) + "     -" + str(montant)
            self.pre_inserer_ligne(str1, str2)
