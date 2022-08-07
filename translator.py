from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="toe", src="english",dest="hindi"):
    text1=text
    sec1=src
    dest1=dest
    trans = Translator()
    trans1 = trans.translate(text, src, dest)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget = change(text= masg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END, textget)
   
root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg='sky blue')

lab_txt=Label(root, text="TRANSLATOR", font=("Ariel", 20, "bold"), bg='sky blue')
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root, text="SOURCE TEXT", font=("Ariel", 15, "bold"), fg='black')
lab_txt.place(x=100,y=100,height=20,width=300)

Sor_txt = Text(frame,font=("Ariel", 10, "bold"),wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)

list_txt = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_txt)
comb_sor.place(x=30,y=300,height=40,width=100)
comb_sor.set("english")

button_change = Button(frame,text="Translate", relief=RAISED, command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_dest = ttk.Combobox(frame,value=list_txt)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("english")

lab_txt=Label(root, text="DESTINATION TEXT", font=("Ariel", 15, "bold"), fg='black')
lab_txt.place(x=100,y=360,height=20,width=300)


dest_txt = Text(frame,font=("Ariel", 10, "bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)


root.mainloop()
