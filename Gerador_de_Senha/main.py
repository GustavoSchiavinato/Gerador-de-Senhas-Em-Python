from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Importando Pillow-------------
from PIL import Image, ImageTk

# Importando Strings-------------
import string

# Importando Random-------------
import random


# Cores ------------------------
cor0 = '#444466' # Preta / Black
cor1 = '#feffff' # Branca / White
cor3 = '#f05a43' # Vermelha / Red

janela = Tk()
janela.title('')
janela.geometry('295x360')
janela.configure(bg=cor1)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Dividindo a Tela em dois frames ------------------------------------------------------
frame_cima = Frame(janela, width=295, height=50, bg=cor1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Trabalhando o Frame Cima ------------------------------------------------------------
img = Image.open('password.png')
img = img.resize((30, 30))
img = ImageTk.PhotoImage(img)

app_logo = Label (frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor1)
app_logo.place(x=2, y=2)

app_nome = Label (frame_cima, text='GERADOR DE SENHAS', width=20, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 16 bold'), bg=cor1, fg=cor0)
app_nome.place(x=45, y=4)

app_linha = Label (frame_cima, text='', width=295, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 1'), bg=cor3, fg=cor0)
app_linha.place(x=0, y=35)

# ------------------------ Função Gerar Senha ------------------------
def criar_senha():

    alfabeto_menor = string.ascii_lowercase
    alfabeto_maior = string.ascii_uppercase
    numeros = '1234567890'
    simbolos = '!@#$%&*-_?/'

    global combinar

    combinar = ''

    #  --- Condição Para Letras Minúsculas ---

    if estado_1.get() == alfabeto_menor:
        combinar = combinar + alfabeto_menor
    else:
        pass

    #  --- Condição Para Letras Maiúsculas ---

    if estado_2.get() == alfabeto_maior:
        combinar = combinar + alfabeto_maior
    else:
        pass

    #  --- Condição Para Números ---

    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass

    #  --- Condição Para Símbolos ---

    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass

    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento))

    app_senha['text'] = senha

    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo("Sucesso", "A Senha Foi Copiada Com Sucesso.")

    botao_copiar_senha = Button (frame_baixo, command=copiar_senha, text='Copiar', width=7, height=2, relief='raised', overrelief='solid', anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
    botao_copiar_senha.grid(row=0, column=1, sticky=NW, padx=5, pady=10, columnspan=1)



# Trabalhando o Frame Baixo ------------------------------------------------------------
app_senha = Label (frame_baixo, text='- - - - -', width=21, height=2, padx=0, relief='solid', anchor='center', font=('Ivy 12 bold'), bg=cor1, fg=cor0)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label (frame_baixo, text='Número Total de Caracteres na Senha', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)


frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=cor1, pady=0, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

alfabeto_menor = string.ascii_lowercase
alfabeto_maior = string.ascii_uppercase
numeros = '1234567890'
simbolos = '!@#$%&*-_?/'

# ------------------------ Letras Minúsculas ------------------------
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=alfabeto_menor, offvalue='off', relief='flat', bg=cor1)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
app_info = Label (frame_caracteres, text='abc - Letras Minúsculas', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5)

# ------------------------ Letras Maiúsculas ------------------------
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, onvalue=alfabeto_maior, offvalue='off', relief='flat', bg=cor1)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
app_info = Label (frame_caracteres, text='ABC - Letras Maiúsculas', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)

# ------------------------ Números ------------------------
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, onvalue=numeros, offvalue='off', relief='flat', bg=cor1)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
app_info = Label (frame_caracteres, text='123 - Números', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=5)

# ------------------------ Símblos ------------------------
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4, onvalue=simbolos, offvalue='off', relief='flat', bg=cor1)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
app_info = Label (frame_caracteres, text='!@# - Símbolos', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=3, column=1, sticky=NW, padx=2, pady=5)


# ------------------------ Botão ------------------------
botao_gerar_senha = Button (frame_caracteres, command=criar_senha, text='Gerar Senha', width=34, height=1, relief='flat', overrelief='solid', anchor='center', font=('Ivy 10 bold'), bg=cor3, fg=cor1)
botao_gerar_senha.grid(row=5, column=0, sticky=NSEW, padx=5, pady=11, columnspan=5)



janela.mainloop()