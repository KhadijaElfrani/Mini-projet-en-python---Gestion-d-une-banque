
class Client:
    def __init__(self):
        self.client_details_list = []
        self.solde = 0
        self.est_connecte = False

    def creer_compte(self, pseudo, telephone, solde_init, mot_de_passe):
        self.solde = solde_init
        conditions = True
        if len(str(telephone)) != 10:
            print("Entrez un num de telephone valide. ")
            conditions = False
        if len(str(mot_de_passe)) != 6:
            print("Entrez un mot de passe de 6 caractères.")
            conditions = False
        if conditions:
            print("Votre compte a bien été crée ! ")
            self.client_details_list = [pseudo, telephone, solde_init, mot_de_passe]
            with open(f"{pseudo}.txt", "w") as f:
                for details in self.client_details_list:
                    f.write(str(details) + "\n")

            with open(f"{pseudo}_releve.txt", "w") as f:
                f.write("Credit initial Creation de compte :     " + str(solde_init))

    def sauthentifier(self, pseudo, telephone, mot_de_passe):
        with open(f"{pseudo}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(telephone) in str(self.client_details_list):
                if str(mot_de_passe) in str(self.client_details_list):
                    self.est_connecte = True
            else:
                print("Les informations sont incorrectes !")
            if self.est_connecte:
                print(f"{pseudo} Bienvenue ! ")
                self.solde = int(self.client_details_list[2])
                self.pseudo = pseudo
