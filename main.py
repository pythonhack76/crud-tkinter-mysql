#crud mysql app


from tkinter import *
from tkinter import ttk
import mysql.connector


root = Tk()
root.title('Crud mySql')
root.geometry('600x450')

#------------------titolo APP ---------------

lblTitolo = Label(root, text="Scheda Cliente", font=('Helvetica', 16), width=30)
lblTitolo.grid(row=1, column=1, columnspan=4)

username = StringVar() 
email = StringVar()
password = StringVar() 



frame = Frame(root, background="white")
frame.grid(row = 0, column=0) 

frame1 = Frame(root, background="light grey")
frame1.grid(row=2, column=0, padx=0, pady=10)


lbl_nome = Label(frame1, text="username", font=("Helvetica", 15))
lbl_nome.grid(row=0, column=0, padx=10, pady=10, sticky="e")

input_nome = Entry(frame1, textvariable=username, font=("Helvetica", 10))
input_nome.grid(row=0, column=1, padx=10, sticky="e")



lbl_email = Label(frame1, text="email", font=("Helvetica", 15))
lbl_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")

input_email = Entry(frame1, textvariable=email, font=("Helvetica", 10))
input_email.grid(row=1, column=1, padx=10, sticky="e")

lbl_password = Label(frame1, text="password", font=("Helvetica", 15))
lbl_password.grid(row=2, column=0, padx=10, pady=10, sticky="e")

input_password = Entry(frame1, textvariable=password, font=("Helvetica", 10))
input_password.grid(row=2, column=1, padx=10, sticky="e")





db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mysql_tk"
    
)

cursore = db.cursor()
cursore.execute("SELECT * FROM utenti")
risultato = cursore.fetchall()

#-------------------------- TREE VIEW -------------------------
colonne = ('id', 'email','username','password')
tabella = ttk.Treeview(root, columns=colonne, show='headings' )
tabella.heading('id', text='ID')
tabella.heading('email', text='EMAIL')
tabella.heading('username', text='USERNAME')
tabella.heading('password', text='PASSWORD')
# 
ausername = username.get('', END)
aemail = email.get('', END)
apassword = password.get('', END)

username.set("username")

for riga in risultato:
    tabella.insert('', END, values=riga)


tabella.grid(row=1, column=0, sticky='nsew')

def inserisci():
    inserisci_sql = "INSERT INTO utenti (email, username, password) VALUES (%s, %s, %s)"
    inserisci_valori = (':username, :email, :password')

    cursore.execute(inserisci_sql, inserisci_valori)
    db.commit() 


def modifica():
    pass

def elimina():
    pass

def chiudi():
    root.destroy() 

inserisci_btn = Button(frame, text="inserisci", bg="red", fg="white", command=inserisci).grid(row=0, column=0, sticky='e')
modifica_btn = Button(frame, text="modifica", bg="yellow", fg="black", command=inserisci).grid(row=0, column=1, sticky='e')
elimina_btn = Button(frame, text="elimina", bg="green", fg="white", command=inserisci).grid(row=0, column=2, sticky='e')
chiudi_btn = Button(frame, text="chiudi", bg="green", fg="white", command=chiudi).grid(row=0, column=3, sticky='e')

root.mainloop() 