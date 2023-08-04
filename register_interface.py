from tkinter import *
from register import UserRegistration
from home_interface import HomeInterface
from login_interface import LoginGUI
import threading

class RegisterInterface:
    def __init__(self):
        self.color = '#61BBAB'
        self.load()
        
    def load(self):
        self.create_screen()
        self.r_background()

        self.create_already_register()
        self.create_titulo()
        self.background_inputs()
        self.create_logo()
        self.create_email_input()
        self.create_name_input()
        self.create_second_name_input()
        self.create_password_input()
        self.create_password_confirm_input()
        self.create_button_register()
        self.window.mainloop()

    def create_screen(self):
        self.window = Tk()
        self.window.title("Cinema Bey")
        self.window.resizable(0,0)
        self.window.geometry("1000x768")

    def background_inputs(self):
        self.img = PhotoImage(file="assets_register/input_bg.png")
        self.input_label = Label(self.window, image=self.img, bg=self.color)
        self.input_label.place(x=550, y=150)

        self.input_label2 = Label(self.window, image=self.img, bg=self.color)
        self.input_label2.place(x=550, y=240)

        self.input_label3 = Label(self.window, image=self.img, bg=self.color)
        self.input_label3.place(x=550, y=340)

        self.input_label4 = Label(self.window, image=self.img, bg=self.color)
        self.input_label4.place(x=550, y=440)

        self.input_label5 = Label(self.window, image=self.img, bg=self.color)
        self.input_label5.place(x=550, y=540)

    def create_email_input(self):
        self.email_input = Entry(self.window, border=0,font=('', 16), width=20)
        self.email_input.place(x=580, y=165)
        self.email_input.insert(0, 'Email')

    def create_name_input(self):
        self.name_input = Entry(self.window, border=0,font=('', 16), width=20)
        self.name_input.place(x=580, y=255)
        self.name_input.insert(0, 'Nome')

    def create_second_name_input(self):
        self.second_name_input = Entry(self.window, border=0,font=('', 16), width=20)
        self.second_name_input.place(x=580, y=355)
        self.second_name_input.insert(0, 'Sobrenome')

    def create_password_input(self):
        self.password_input = Entry(self.window, show="*", border=0,font=('', 16), width=20)
        self.password_input.place(x=580, y=455)
        self.password_input.insert(0, 'Password')

    def create_password_confirm_input(self):
        self.password_confirm_input = Entry(self.window, show="*", border=0,font=('', 16), width=20)
        self.password_confirm_input.place(x=580, y=555)
        self.password_confirm_input.insert(0, "Password")
    
    def create_button_register(self):
        self.button_register_img = PhotoImage(file="assets_register/button_bg.png")
        self.button_register = Button(self.window, image=self.button_register_img, border=0, bg=self.color, activebackground=self.color,command=lambda:threading.Thread(target=self.register).start())
        self.button_register.place(x=780, y=655) #button
        

    def create_titulo(self):
        self.titulo_img = PhotoImage(file="assets_register/titulo.png")
        self.titulo_register = Label(self.window, image=self.titulo_img, bg=self.color)
        self.titulo_register.place(x=634, y=50)

    def create_logo(self):
        self.logo_register_img = PhotoImage(file="assets_register/logo.png")
        self.logo_register = Label(self.window, image=self.logo_register_img, bg="#FFFFFF") 
        self.logo_register.place(x=80, y=355)

    def create_message_error(self):
        self.message_regsiter = Label(self.window, text="Email já cadastrado ou Confirmação de senha invalida!", bg=self.color, fg="red")                
        self.message_regsiter.place(x=555, y=610)
    
    def create_already_register(self):
        self.button_al_register = Button(self.window, text="Já tem uma conta?", font="'' 12",border=0, activebackground=self.color, bg=self.color, fg="black", command=lambda:self.already())
        self.button_al_register.place(x=481, y=666)

    def already(self):
        import os
        path = os.path.join("login_interface.py")
        os.system("python "+path)
        
    def r_background(self):
        self.background_img = PhotoImage(file="assets_register/background.png")
        self.label_r_background = Label(self.window, image=self.background_img)
        self.label_r_background.place(x=0, y=-2)    
    
    def register(self):
        r = UserRegistration()
        self.email = self.email_input.get()
        self.name = self.name_input.get()
        self.second_name = self.second_name_input.get()
        self.password = self.password_input.get()
        self.password_confirm = self.password_confirm_input.get()
        r.setData(f"{self.email}".lower(), f"{self.name}".lower(), f"{self.second_name}".lower(), f"{self.password}", f"{self.password_confirm}")
        if r.registred == True:
            print('Registred successfully!')
            r.registred = False
            HomeInterface(self.email)    
        else:
            self.create_message_error()
               
if __name__ == "__main__":
    RegisterInterface()