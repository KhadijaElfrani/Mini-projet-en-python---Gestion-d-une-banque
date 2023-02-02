from tkinter import *
from Client import Client
from fpdf import FPDF  # pip install fpdf
from Operation import Operation


mon_client = Client()
mon_operation = Operation()

# telecharger le releve en format pdf
def telecharger_releve():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.cell(200, 20, txt="Releve de compte de " + str(mon_client.pseudo), ln=1, align="C")
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 5, txt="Pseudo : " + str(mon_client.pseudo), ln=1, align="L")
    pdf.cell(200, 5, txt="Numero de telephone " + str(mon_client.client_details_list[1]), ln=1, align="L")
    pdf.cell(200, 5, txt="Solde actuel : " + str(mon_client.solde), ln=1, align="L")
    pdf.set_font("Arial", size=20)
    pdf.cell(200, 20, txt="Operations", ln=1, align="C")
    pdf.set_font("Arial", size=10)
    with open(f"{mon_client.pseudo}_releve.txt", "r") as f:
        for x in f:
            pdf.cell(200, 10, txt=x, ln=1, align='L')

    pdf.output(str(mon_client.pseudo) + "_releve.pdf")

# effacer le contenu de la fenetre
def clear_frame():
    for widgets in fenetre.winfo_children():
        widgets.destroy()

# verifier les informations entrées et creation du compte
def verifier_informations_et_creer_compte():
    p = pseudo.get()
    t = telephone.get()
    si = solde_init.get()
    m = mot_de_passe.get()
    mv = mot_de_passe_verifier.get()
    canvas = Canvas(fenetre, width=300, height=20, bg='#df8fff', highlightthickness=0)
    if len(str(p)) < 4 or len(str(p)) > 10:
        canvas.place(x=20, y=450)
        Label(fenetre, text="*Le pseudo doit contenir entre 4 et 10 caractères", font=("Arial", 10), bg='#df8fff',
              fg='red').place(x=20, y=450)
    elif len(str(t)) != 10:
        canvas.place(x=20, y=450)
        Label(fenetre, text="*Le numero telephone doit contenir 10 chiffres", font=("Arial", 10), bg='#df8fff',
              fg='red').place(x=20, y=450)
    elif not si or int(si) < 0:
        canvas.place(x=20, y=450)
        Label(fenetre, text="*valeur de solde initial non valide", font=("Arial", 10), bg='#df8fff',
              fg='red').place(x=20, y=450)

    elif str(m) != str(mv) or not m or not mv:
        canvas.place(x=25, y=450)
        Label(fenetre, text="*Les mots de passe ne correspondent pas !", font=("Arial", 10), bg='#df8fff',
              fg='red').place(x=20, y=450)
    else:
        mon_client.creer_compte(p, t, si, m)
        accueil_interface()

# verifier les informations entrés et authentification
def verifier_informations_et_sauthentifier():
    p = pseudo.get()
    t = telephone.get()
    m = mot_de_passe.get()
    canvas = Canvas(fenetre, width=300, height=20, bg='#df8fff', highlightthickness=0)
    if len(str(p)) < 4 or len(str(p)) > 10:
        canvas.place(x=20, y=450)
        Label(fenetre, text="*Le pseudo doit contenir entre 4 et 10 caractères", font=("Arial", 10), bg='#df8fff',
              fg='red').place(x=20, y=450)
    elif len(str(t)) != 10:
        canvas.place(x=20, y=450)
        Label(fenetre, text="*Le numero telephone doit contenir 10 chiffres", font=("Arial", 10), bg='#df8fff',
              fg='red').place(x=20, y=450)
    elif not m:
        canvas.place(x=20, y=450)
        Label(fenetre, text="*Veuiullez saisir votre mot de passe", font=("Arial", 10), bg='#df8fff',
              fg='red').place(x=20, y=450)
    else:
        with open(f"{p}.txt", "r") as f:
            details = f.read()
            mon_client.client_details_list = details.split("\n")
            if str(t) in str(mon_client.client_details_list):
                if str(m) in str(mon_client.client_details_list):
                    mon_client.sauthentifier(p, t, m)
                    bienvenue_interface()
            else:
                canvas.place(x=20, y=450)
                Label(fenetre, text="*Informations incorrectes", font=("Arial", 10),
                      bg='#df8fff', fg='red').place(x=20, y=450)

# l'interface de base
def accueil_interface():
    clear_frame()
    fenetre.title("La banque")
    fenetre.geometry("700x600")
    fenetre.config(background='#9E00D5')
    # fenetre.eval('tk::PlaceWindow . center')
    global acceuil_img
    acceuil_img = PhotoImage(file="1.png")
    l = Label(fenetre, image=acceuil_img)
    l.place(x=0, y=0)

    # Ajoute de texte
    Label(fenetre, text="Bienvenue à votre Banque !", font=("Arial", 30), bg='#9E00D5', fg='white').place(x=20, y=20)
    # Ajoute de bouton
    bouton_sauthentifier = Button(text="S'authentifier", font=("Arial", 20), bg='white', fg='#9E00D5',
                                  command=sauthentifier_interface)
    bouton_creer_compte = Button(text="Créer un compte", font=("Arial", 20), bg='white', fg='#9E00D5',
                                 command=creer_compte_interface)
    bouton_sauthentifier.place(x=250, y=200)
    bouton_creer_compte.place(x=230, y=300)

# interface d'authentification
def sauthentifier_interface():
    global pseudo
    global telephone
    global mot_de_passe
    pseudo = StringVar()
    telephone = StringVar()
    mot_de_passe = StringVar()
    clear_frame()
    fenetre.config(background='#df8fff')
    Label(fenetre, text="AUTHENTIFICATION", font=("Arial", 30), bg='#df8fff', fg='white').pack()

    label_pseudo = Label(fenetre, text="Votre Pseudo : ", font=("Arial", 15), bg='#df8fff', fg='black')
    label_pseudo.place(x=50, y=200)
    Entry(fenetre, width=40, textvariable=pseudo).place(x=350, y=200)

    label_telephone = Label(fenetre, text="Votre Numero de telephone : ", font=("Arial", 15), bg='#df8fff', fg='black')
    label_telephone.place(x=50, y=250)
    Entry(fenetre, width=40, textvariable=telephone).place(x=350, y=250)

    label_mot_de_passe = Label(fenetre, text="Votre Mot de passe : ", font=("Arial", 15), bg='#df8fff', fg='black')
    label_mot_de_passe.place(x=50, y=300)
    Entry(fenetre, width=40, show="*", textvariable=mot_de_passe).place(x=350, y=300)

    bouton_connexion = Button(text="Connexion", font=("Arial", 20), bg='white', fg='#9E00D5',
                              command=verifier_informations_et_sauthentifier)
    bouton_connexion.place(x=250, y=500)

    bouton_accueil = Button(text="Accueil", font=("Arial", 10), bg='white', fg='#9E00D5', command=accueil_interface)
    bouton_accueil.place(x=20, y=20)

# interface de creation du compte
def creer_compte_interface():
    global pseudo
    global telephone
    global mot_de_passe
    global solde_init
    global mot_de_passe_verifier
    pseudo = StringVar()
    telephone = StringVar()
    mot_de_passe = StringVar()
    mot_de_passe_verifier = StringVar()
    solde_init = StringVar()
    clear_frame()
    fenetre.config(background='#df8fff')
    Label(fenetre, text="CREATION DU COMPTE", font=("Arial", 30), bg='#df8fff', fg='white').pack()

    label_pseudo = Label(fenetre, text="Votre Pseudo : ", font=("Arial", 15), bg='#df8fff', fg='black')
    label_pseudo.place(x=50, y=200)
    Entry(fenetre, width=40, textvariable=pseudo).place(x=350, y=200)

    label_telephone = Label(fenetre, text="Votre Numero de telephone : ", font=("Arial", 15), bg='#df8fff', fg='black')
    label_telephone.place(x=50, y=250)
    Entry(fenetre, width=40, textvariable=telephone).place(x=350, y=250)

    label_solde_init = Label(fenetre, text="Choisissez votre solde initial : ", font=("Arial", 15), bg='#df8fff',
                             fg='black')
    label_solde_init.place(x=50, y=300)
    Entry(fenetre, width=40, textvariable=solde_init).place(x=350, y=300)

    label_mot_de_passe = Label(fenetre, text="Choisir votre Mot de passe : ", font=("Arial", 15), bg='#df8fff',
                               fg='black')
    label_mot_de_passe.place(x=50, y=350)
    Entry(fenetre, width=40, show="*", textvariable=mot_de_passe).place(x=350, y=350)

    label_mot_de_passe_verifier = Label(fenetre, text="Vérifier Mot de passe : ", font=("Arial", 15), bg='#df8fff',
                                        fg='black')
    label_mot_de_passe_verifier.place(x=50, y=400)
    Entry(fenetre, width=40, show="*", textvariable=mot_de_passe_verifier).place(x=350, y=400)

    bouton_connexion = Button(text="Creer compte", font=("Arial", 20), bg='white', fg='#9E00D5',
                              command=verifier_informations_et_creer_compte)
    bouton_connexion.place(x=250, y=500)

    bouton_accueil = Button(text="Accueil", font=("Arial", 10), bg='white', fg='#9E00D5', command=accueil_interface)
    bouton_accueil.place(x=20, y=20)


# fonction pour effacer la zone en bas de l'interface bienvenue
def effacer_zone():
    canvas = Canvas(fenetre, width=580, height=200, bg='#F0BAFF', highlightthickness=0)
    canvas.place(x=20, y=400)

# formulaire pour Créditer
def crediter_forme():
    global montant
    global motif
    montant = IntVar()
    motif = StringVar()
    effacer_zone()
    Label(fenetre, text="CREDITER", font=("Arial", 20), bg='#F0BAFF', fg='white').place(x=40, y=410)

    Label(fenetre, text="Le montant à créditer : ", font=("Arial", 15), bg='#F0BAFF', fg='black').place(x=50, y=460)
    Entry(fenetre, width=40, textvariable=montant).place(x=350, y=460)

    Label(fenetre, text="Motif de crédit : ", font=("Arial", 15), bg='#F0BAFF', fg='black').place(x=50, y=490)
    Entry(fenetre, width=40, textvariable=motif).place(x=350, y=490)

    bouton_confirmer = Button(text="Confirmer", font=("Arial", 10), bg='white', fg='#9E00D5',
                              command=verifier_et_crediter)
    bouton_confirmer.place(x=400, y=550)

    bouton_annuler = Button(text="Annuler", font=("Arial", 10), bg='white', fg='#9E00D5', command=effacer_zone)
    bouton_annuler.place(x=500, y=550)

def verifier_et_crediter():
    m = montant.get()
    mtf = motif.get()
    if m > 0:
        mon_operation.ajouter_solde(m, mon_client, mtf)
        affiche_solde()
        alerte_success()
    else:
        alerte_echec()


def verifier_et_debiter():
    m = montant.get()
    mtf = motif.get()
    if m > 0 and m <= mon_client.solde:
        mon_operation.debiter_solde(m, mon_client, mtf)
        affiche_solde()
        alerte_success()
    else:
        alerte_echec()


def verifier_et_transferer():
    m = montant.get()
    pc = pseudo_cible.get()
    tc = tele_cible.get()
    if m > 0 and m <= mon_client.solde:
        mon_operation.effectuer_virement(m, pc, tc, mon_client)
        affiche_solde()
        alerte_success()
    else:
        alerte_echec()


def alerte_success():
    alert = Tk()
    alert.geometry("300x100")
    alert.config(bg="#F0BAFF")
    alert.title("success !")
    Button(alert, text="Close", font=("Arial", 10), bg='white', fg='black', command=alert.destroy).place(x=120, y=60)
    Label(alert, text="Operation effectué avec success. ", bg='#F0BAFF', fg='black', font=("Arial", 10)).place(x=40,
                                                                                                               y=20)


def alerte_echec():
    alert = Tk()
    alert.geometry("300x100")
    alert.config(bg="#F0BAFF")
    alert.title("erreur !")
    Button(alert, text="Close", font=("Arial", 10), bg='white', fg='black', command=alert.destroy).place(x=120, y=60)
    Label(alert, text="Echec d'effectuer l'operation.", bg='#F0BAFF', fg='black', font=("Arial", 10)).place(x=60, y=10)
    Label(alert, text="Veuillez vérifier votre saisie. ", bg='#F0BAFF', fg='black', font=("Arial", 10)).place(x=60,
                                                                                                              y=30)


def afficher_operations():
    # affiche que les 5 derniers operations :
    i = 0
    k = 0
    effacer_zone()
    Label(fenetre, text="OPERATIONS RÉCENTES", font=("Arial", 20), bg='#F0BAFF', fg='white').place(x=40, y=410)
    Button(text="Afficher tout", font=("Arial", 10), bg='white', fg='#9E00D5',
           command=afficher_toutes_operations).place(x=600, y=410)
    with open(f"{mon_client.pseudo}_releve.txt", "r") as f:
        operations = f.read()
        mon_operation.liste_operations = operations.split("\n")
        for operation in mon_operation.liste_operations:
            if "+" in str(operation):
                couleur = 'green'
            elif "-" in str(operation):
                couleur = 'red'
            if k < 5:
                Label(fenetre, text=operation, font=("Arial", 10), bg='#F0BAFF', fg=couleur).place(x=40, y=450 + i)
                i += 20
                k += 1
            else:
                break


def afficher_toutes_operations():
    # affiche toutes les operations dans une autre fenetre
    operations_fenetre = Tk()
    operations_fenetre.geometry("300x600")
    operations_fenetre.config(bg="#F0BAFF")
    operations_fenetre.title("Toutes mes operations")
    i = 0
    with open(f"{mon_client.pseudo}_releve.txt", "r") as f:
        operations = f.read()
        mon_operation.liste_operations = operations.split("\n")
        for operation in mon_operation.liste_operations:
            if "+" in str(operation):
                couleur = 'green'
            elif "-" in str(operation):
                couleur = 'red'
            Label(operations_fenetre, text=operation, font=("Arial", 10), bg='#F0BAFF', fg=couleur).place(x=20,y=40 + i)
            i += 30

def debiter_forme():
    global montant
    global motif
    montant = IntVar()
    motif = StringVar()
    effacer_zone()
    Label(fenetre, text="DEBITER", font=("Arial", 20), bg='#F0BAFF', fg='white').place(x=40, y=410)

    Label(fenetre, text="Le montant à débiter : ", font=("Arial", 15), bg='#F0BAFF', fg='black').place(x=50, y=460)
    Entry(fenetre, width=40, textvariable=montant).place(x=350, y=460)

    Label(fenetre, text="Motif de débit : ", font=("Arial", 15), bg='#F0BAFF', fg='black').place(x=50, y=490)
    Entry(fenetre, width=40, textvariable=motif).place(x=350, y=490)

    bouton_confirmer = Button(text="Confirmer", font=("Arial", 10), bg='white', fg='#9E00D5',
                              command=verifier_et_debiter)
    bouton_confirmer.place(x=400, y=550)

    bouton_annuler = Button(text="Annuler", font=("Arial", 10), bg='white', fg='#9E00D5', command=effacer_zone)
    bouton_annuler.place(x=500, y=550)


def effectuer_virement_forme():
    global montant
    global pseudo_cible
    global tele_cible

    montant = IntVar()
    pseudo_cible = StringVar()
    tele_cible = StringVar()

    effacer_zone()
    Label(fenetre, text="EFFECTUER VIREMENT", font=("Arial", 20), bg='#F0BAFF', fg='white').place(x=40, y=410)

    Label(fenetre, text="Le pseudo de destinataire: ", font=("Arial", 15), bg='#F0BAFF', fg='black').place(x=50, y=460)
    Entry(fenetre, width=40, textvariable=pseudo_cible).place(x=350, y=460)
    Label(fenetre, text="Son numéro de téléphone: ", font=("Arial", 15), bg='#F0BAFF', fg='black').place(x=50, y=490)
    Entry(fenetre, width=40, textvariable=tele_cible).place(x=350, y=490)
    Label(fenetre, text="Le montant à envoyer: ", font=("Arial", 15), bg='#F0BAFF', fg='black').place(x=50, y=520)
    Entry(fenetre, width=40, textvariable=montant).place(x=350, y=520)

    bouton_confirmer = Button(text="Confirmer", font=("Arial", 10), bg='white', fg='#9E00D5',
                              command=verifier_et_transferer)
    bouton_confirmer.place(x=400, y=550)

    bouton_annuler = Button(text="Annuler", font=("Arial", 10), bg='white', fg='#9E00D5', command=effacer_zone)
    bouton_annuler.place(x=500, y=550)


def affiche_solde():
    Label(fenetre, text="Solde : " + str(mon_client.solde) + ".00 €    ", font=("Arial", 20), bg='white',
          fg='green').place(x=400, y=150)


def bienvenue_interface():
    clear_frame()
    global img
    p = pseudo.get()
    img = PhotoImage(file="2.png")
    l = Label(fenetre, image=img)
    l.place(x=0, y=0)
    Label(fenetre, text="Bienvenue dans votre espace " + str(p) + " !", font=("Arial", 20), bg='white',
          fg='black').place(x=20, y=20)
    affiche_solde()
    Button(text="Créditer", font=("Arial", 10), fg='white', bg='#9E00D5', width=15, height=2,
           command=crediter_forme).place(x=15, y=300)
    Button(text="Débiter", font=("Arial", 10), fg='white', bg='#9E00D5', width=15, height=2,
           command=debiter_forme).place(x=150, y=300)
    Button(text="Effectuer Virement", font=("Arial", 10), fg='white', bg='#9E00D5', width=15, height=2,
           command=effectuer_virement_forme).place(x=285, y=300)
    Button(text="Operations récentes", font=("Arial", 10), fg='white', bg='#9E00D5', width=15, height=2,
           command=afficher_operations).place(x=420, y=300)
    Button(text="Télécharger relevé", font=("Arial", 10), fg='white', bg='#9E00D5', width=15, height=2,
           command=telecharger_releve).place(x=555, y=300)


# creation de la fenetre :
fenetre = Tk()
accueil_interface()
# Affichage de la fenetre
fenetre.mainloop()
