from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb  # Biblioteca para ocultação de dados em imagens

# Inicializa a janela principal do tkinter
root = Tk()

# Define o título da janela
root.title("Steganography")

# Define o tamanho da janela
root.geometry("700x500+250+180")

# Impede a redimensionamento da janela
root.resizable(False, False)

# Define a cor de fundo da janela
root.configure(bg="#2f4155")

# Função para abrir e exibir uma imagem
def showimage():
    global filename
    # Abre um diálogo para o usuário escolher uma imagem
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetypes=(("PNG file", "*.png"), ("JPG.file", "*.jpg"), ("All file", "*.txt")))
    
    # Abre a imagem escolhida e converte para um formato compatível com tkinter
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    
    # Exibe a imagem na interface
    lb1.configure(image=img, width=250, height=250)
    lb1.image = img

# Função para ocultar uma mensagem na imagem usando esteganografia
def Hide():
    global secret
    # Obtém o texto a ser escondido da caixa de texto
    Message = text1.get(1.0, END)
    # Esconde a mensagem na imagem usando a função hide da biblioteca lsb
    secret = lsb.hide(str(filename), Message)

# Função para revelar a mensagem escondida na imagem
def Show():
    # Revele a mensagem da imagem usando a função reveal da biblioteca lsb
    clear_message = lsb.reveal(filename)
    # Limpa a caixa de texto antes de inserir a mensagem revelada
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

# Função para salvar a imagem com a mensagem oculta
def save():
    # Salva a imagem com a mensagem oculta no arquivo "hidden.png"
    secret.save("hidden.png")

# Definir o ícone da janela
image_icon = PhotoImage(file="image/investigacao.png")
root.iconphoto(False, image_icon)

# Exibir um logo na janela
logo = PhotoImage(file="image/digitalizacao-de-impressao-digital.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

# Exibir o título "CYBER SCIENCE"
Label(root, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

# Primeira Frame: para exibir a imagem escolhida
f = Frame(root, bd=1, width=340, height=280, relief="groove", bg="black")
f.place(x=10, y=80)
lb1 = Label(f, bg="black")
lb1.place(x=40, y=10)

# Segunda Frame: para exibir e editar a mensagem a ser oculta
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)
text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

# Adicionar barra de rolagem para a caixa de texto
scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Terceira Frame: para exibir os botões de abrir e salvar imagem
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)
Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo file", bg="#2f4155", fg='yellow').place(x=20, y=5)

# Quarta Frame: para exibir os botões de esconder e revelar a mensagem
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=3600, y=370)
Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(frame4, text="Picture, Image, Photo file", bg="#2f4155", fg='yellow').place(x=20, y=5)

# Inicia o loop principal da interface gráfica
root.mainloop()
