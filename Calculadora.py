#Maria Jennifer Carbajal Martinez 41s
#Lorenzo Hernandez Hernandez 41s
#Calculadora
from tkinter import*

raiz = Tk()
raiz.title("JMBE2003")
raiz.geometry("350x400")

frame = Frame(raiz)
frame.config(width="600px",height="300px")
frame.pack(fill="both",expand=1)

titule = Label(frame,text="CALCULADORA ",font=("Vanilla Caramel",15,"bold"))
titule.pack(side=TOP)
num1 = StringVar()
num2= StringVar()
ru= StringVar()

def sumar():
  ru.set(float(num1.get())+float(num2.get()))
   
def resta():
  ru.set(float(num1.get())-float(num2.get()))
   
def multiplicar():
  ru.set(float(num1.get())*float(num2.get()))
    
def divide():
  ru.set(float(num1.get())/float(num2.get()))
   
def borrar():
  entrada_numeroaa=Entry(raiz, textvariable= " ").place(relx=0.4,rely=0.2)
  entrada_numerobb=Entry(raiz, textvariable= " ").place(relx=0.4,rely=0.3)   
  entrada_resultadoo=Entry(raiz, textvariable= " ").place(relx=0.4,rely=0.4)
   
lbl_numberone = Label(raiz, text="Number one",font=("Vanilla Caramel",15,"bold")).place(relx=0.1,rely=0.2)

entry_numeberone = Entry(raiz,textvariable=num1).place(relx=0.4,rely=0.2)

lbl_numbertwo = Label(raiz, text="Number two",font=("Vanilla Caramel",15,"bold")).place(relx=0.1,rely=0.3)

entry_numerobb = Entry(raiz,textvariable=num2).place(relx=0.4,rely=0.3)

lbl_resultado = Label(raiz, text="Result",font=("Vanilla Caramel",15,"bold")).place(relx=0.2,rely=0.4)

entry_result = Entry(raiz,textvariable=ru).place(relx=0.4,rely=0.4)

rbt_sum = Button(raiz, text="     +     ",command=sumar,bg="#CC3300").place(relx=0.2,rely=0.5)

rbt_mult = Button(raiz, text="     x     ",command=multiplicar,bg="#CC3300") .place(relx=0.4,rely=0.5)

rbt_delete = Button(raiz, text="     c     ",command=borrar,bg="#CC3300").place(relx=0.6,rely=0.5)

rbt_split = Button(raiz, text="     /     ", command=divide,bg="#CC3300").place(relx=0.2,rely=0.6)

rbt_subtract = Button(raiz, text="     -     ",command=resta,bg="#CC3300").place(relx=0.4,rely=0.6)

rbt_equal = Button(raiz, text="     =     ",bg="#CC3300").place(relx=0.6,rely=0.6)

raiz.mainloop()