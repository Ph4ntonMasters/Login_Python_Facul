import customtkinter as ctk
from tkinter import *

janela = ctk.CTk()


class Application():

    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de Login")
        janela.resizable(False, False)

    def tela_login(self):

        #Trabalhando com a Imagem da tela
        img = PhotoImage(file="png-transparent-logo-contracting-photography-logo-symbol.png")
        label_img = ctk.CTkLabel(master=janela, image=img)
        label_img.place(x=5, y=65)

        çabel_tt = ctk.CTkLabel(master=janela, text="Entre na sua conta e tenha\n acesso a Plataforma",
                                        font=("Roboto",18), text_color="#00B0F0").place(x=10,y=10)

        #frame
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        #widgets dentro da frame de login
        label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=('Roboto', 20, 'bold'), text_color= ('white'))
        label.place(x=25, y=5)

        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de Usuário", width=300, font=("Roboto", 14)).place(x=25, y=105)
        username_label = ctk.CTkLabel(master=login_frame, text="*O campo nome de usuário é obrigatorio!", text_color="green", font=("Roboto", 8)).place(x=25,y=135)

        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", width=300, font=("Roboto", 14), show="*").place(x=25, y=175)
        password_label = ctk.CTkLabel(master=login_frame, text="*O campo Senha é obrigatorio!", text_color="green", font=("Roboto", 8)).place(x=25,y=205)

        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembrar minha senha").place(x=25, y=235)

        login_button = ctk.CTkButton(master=login_frame, text="Login", width=300).place(x=25,y=285)



Application()