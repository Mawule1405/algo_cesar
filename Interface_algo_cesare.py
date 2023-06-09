import Application_algo_cesare
import tkinter
import tkinter.messagebox

niveau1 =0
niveau2=0


def cryptage():
    
    key = cle_pour_crypter.get()
    msg = msg_a_crypter.get()
    msg_a_decrypter.delete(0,tkinter.END)
    cle_pour_decrypter.delete(0,tkinter.END)
    if len(key)>4 :
        tkinter.messagebox.showerror("Attention!!!  ","Votre clé est invalidée")
    elif len(key)==0:
        tkinter.messagebox.showerror("Attention!!!  ","Veuillez entrer une clé ou faire un cryptage sans clé")
    else:
        try:
            key = int(key)
            msg_decrypter = Application_algo_cesare.algo_cryptage_de_cesare(msg,key)
            msg_a_decrypter.insert(0,msg_decrypter)
        except:
            tkinter.messagebox.showerror("Attention!!!  ","Votre clé est invalidé")



def decryptage():
    key = cle_pour_decrypter.get()
    msg = msg_a_decrypter.get()
    msg_a_crypter.delete(0,tkinter.END)
    cle_pour_crypter.delete(0,tkinter.END)
    if len(key)>4:
        msg_a_crypter.insert(0,"Clé invalide")   
    else:
        try:
            key = int(key)
            msg_crypter = Application_algo_cesare.algo_decryptage_de_cesare(msg,key)
            msg_a_crypter.insert(0,msg_crypter)
        except:
            msg_a_crypter.insert(0,"Clé invalide")


def decryptage_sans_cle():
    global niveau2
    msg = msg_a_decrypter.get()
    msg_a_crypter.delete(0,tkinter.END)
    cle_pour_crypter.delete(0,tkinter.END)
    reponse = valeur2.get()
    niveau2+=reponse 
    msg_decrypter = Application_algo_cesare.algo_decryptage_de_cesare(msg,niveau2)
    msg_a_crypter.insert(0,msg_decrypter)
    cle_pour_decrypter.delete(0,tkinter.END)
    cle_pour_decrypter.insert(0,str(niveau2))

def cryptage_sans_cle():
    global niveau1
    msg = msg_a_crypter.get()
    msg_a_decrypter.delete(0,tkinter.END)
    cle_pour_decrypter.delete(0,tkinter.END)
    reponse = valeur1.get()
    niveau1+=reponse 
    msg_crypter = Application_algo_cesare.algo_cryptage_de_cesare(msg,niveau1)
    msg_a_decrypter.insert(0,msg_crypter)
    cle_pour_crypter.delete(0,tkinter.END)
    #cle_pour_decrypter.insert(0,str(niveau))       

#Verification des valeurs des checkbox pour qu'il ne se croche pas au meme moment
def chercker(v1,v2):
    if v1.get():
        v2.set(0)
    elif v2.get():
        v1.set(0)

def quitter():
    reponse=tkinter.messagebox.askquestion(title="Effacer",message="Voulez vous fermer\nl'application")       
    if reponse == "yes":
        windows.quit()


def effacer():
    reponse=tkinter.messagebox.askquestion(title="Effacer",message="Voulez vous effacer\n les champs de saisis?")       
    if reponse == "yes":
        msg_a_crypter.delete(0,tkinter.END)
        msg_a_decrypter.delete(0,tkinter.END)
        cle_pour_crypter.delete(0,tkinter.END)
        cle_pour_decrypter.delete(0,tkinter.END)
    

windows = tkinter.Tk()
windows.title("Cryptage et Décryptage de CESAR")               #titre de la fenetre
largeur,hauteur = 700,350
larg,haut  = 1100,500
x,y = (larg-largeur),(haut-hauteur) 
windows.geometry(f"{largeur}x{hauteur}+{x}+{y}")                                    #taille de la fenetre
windows.resizable(width=False,height=False)
#windows.iconbitmap("photo/photo_cesar.ico")                           #icone de la fenetre
windows.configure(bg="light blue")
#fond_image = tkinter.PhotoImage(file="photo2_cesar.jpg")          #Image de fond de la fenetre

#fond_ecran = tkinter.canvas(windows,width=700 ,height=300)       #Fond d'ecran de la fenetre
#fond_ecran.create_image(0,0, image= fond_image, anchor=tkinter.NW)
"""Les couleurs et les fonts"""
col_frame = "#87dec6"
col_entry = "white"
col_fg_entry = "black"
col_label = "#87dec6"
col_fg_label = "black"
col_label_t ="light blue"
col_fg_label_t="red"
font_label = "Times  11 bold"
font_entry = "Times 13 bold"

"""En tete de la fenetre: Titre"""
entete = tkinter.Label(windows, text="Cryptage et décryptage par algorithme de Cesar",width=40,height=2, font="broadway 15",fg="black",bg="light blue")
entete.pack()

"""Zone d'affichage des messages"""
frame1 = tkinter.Frame(windows, width=680,height=80,bg=col_frame,borderwidth=1,relief="sunken")
frame1.place(x=10,y=50)
cryp_lab = tkinter.Label(windows,text="Zone des messages cryptés",bd=1,relief="sunken",bg=col_label_t,fg=col_fg_label_t,font=font_label)
cryp_lab.place(x=30,y=40)

"""Pour la zone de texte: message a crypter """
ettiquette_cle = tkinter.Label(frame1,width=2, height=1 ,text="clé",bg=col_label, fg=col_fg_label, font=font_label)
ettiquette_cle.place(x=10,y=10)
cle_pour_crypter  = tkinter.Entry(frame1, width=5,bg=col_entry, fg=col_fg_entry, font=font_entry)
cle_pour_crypter.place(x=10,y=40)
ettiquette_msg_crypter = tkinter.Label(frame1,width=13, height=1,text="Message a crypté",bg=col_label, fg=col_fg_label, font=font_label)
ettiquette_msg_crypter.place(x=100,y=10)
msg_a_crypter = tkinter.Entry(frame1, width=25,bg=col_entry, fg=col_fg_entry, font=font_entry)
msg_a_crypter.place(x=100,y=40)

"""Pour la zone de texte: message a decrypter """
decryp_lab = tkinter.Label(windows,text="Zone des messages décryptés",bd=1,relief="sunken",bg=col_label_t,fg=col_fg_label_t,font=font_label)
decryp_lab.place(x=400,y=40)

ettiquette_cle2 = tkinter.Label(frame1,width=2, height=1 ,text="clé",bg=col_label, fg=col_fg_label, font=font_label)
ettiquette_cle2.place(x=600,y=10)
cle_pour_decrypter  = tkinter.Entry(frame1, width=5,bg=col_entry, fg=col_fg_entry, font=font_entry)
cle_pour_decrypter.place(x=600,y=40)
ettiquette_msg_decrypter = tkinter.Label(frame1,width=14, height=1 ,text="Message a decrypté",bg=col_label, fg=col_fg_label, font=font_label)
ettiquette_msg_decrypter.place(x=350,y=10)
msg_a_decrypter = tkinter.Entry(frame1, width=25,bg=col_entry, fg=col_fg_entry, font=font_entry)
msg_a_decrypter.place(x=350,y=40)

""" Les boutons """
frame2 = tkinter.Frame(windows, width=680,height=60,bg=col_frame,borderwidth=1,relief="sunken")
frame2.place(x=10,y=260)
btn_lab_cle = tkinter.Label(windows,text="Zone de cryptage et décryptage avec clé",bd=1,relief="sunken",bg=col_label_t,fg=col_fg_label_t,font=font_label)
btn_lab_cle.place(x=30,y=250)

bnt_cryptage = tkinter.Button(frame2, text="CRYPTER",width=10,height=1, bg="yellowgreen", fg="black", font="bold 13 normal", command=cryptage).place(x=10,y=15)
bnt_effacer = tkinter.Button(frame2, text="EFFACER",width=10,height=1, bg="yellowgreen", fg="black", font="bold 13 normal",command=effacer).place(x=200,y=15)
bnt_quitter = tkinter.Button(frame2, text="QUITTER",width=10,height=1, bg="yellowgreen", fg="black", font="bold 13 normal",command=quitter).place(x=370,y=15)
bnt_decrypter = tkinter.Button(frame2, text="DECRYPTER",width=12,height=1, bg="yellowgreen", fg="black", font="bold 13 normal",command=decryptage).place(x=540,y=15)

"""Zone de cryptage et décryptage sans clé"""
frame3 = tkinter.Frame(windows, width=680,height=60,bg=col_frame,borderwidth=1,relief="sunken")
frame3.place(x=10,y=160)
btn_lab_s_cle = tkinter.Label(windows,text="Zone de cryptage et décryptage sans clé",bd=1,relief="sunken",bg=col_label_t,fg=col_fg_label_t,font=font_label)
btn_lab_s_cle.place(x=30,y=150)

"""Les checkboxs"""
valeur1 = tkinter.IntVar()
new_valide1=tkinter.Checkbutton(frame3,variable=valeur1,bg=col_frame)
new_valide1.place(x=200,y=20)
valeur2 = tkinter.IntVar()
new_valide2=tkinter.Checkbutton(frame3,variable=valeur2,bg=col_frame)
new_valide2.place(x=450,y=20)
valeur1.trace_add('write',lambda *args:chercker(valeur1,valeur2))
valeur2.trace_add('write',lambda *args:chercker(valeur2,valeur1))

"""Bouton de cryptage sans cle"""
new_btn1 = tkinter.Button(frame3, text=f"Crypter sans clé",width=15,height=1, bg="yellowgreen", fg="black", font="bold 13 normal",command=cryptage_sans_cle)
new_btn1.place(x=10, y = 15)

"""Bouton de decryptage sans cle"""
new_btn2 = tkinter.Button(frame3, text=f"Décrypter sans clé",width=15,height=1, bg="yellowgreen", fg="black", font="bold 13 normal", command=decryptage_sans_cle)
new_btn2.place(x=520, y = 15)



windows.mainloop()