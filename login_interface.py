from tkinter import *
from login import LoginUser
import threading
from home_interface import HomeInterface

class LoginGUI:
    def __init__(self):
        self.color = "#4E88A0"
        self.load()

    def load(self):
        self.create_screen()
        self.create_email_input()
        self.create_password_input()
        self.create_button_login()
        self.create_logo()
        self.window.mainloop()

    def create_screen(self):
        self.window = Tk()
        self.window.title("Login Page")
        self.window.resizable(0,0)
        self.window.geometry("1000x768")
        self.window.config(bg="#FFFFFF")

    def create_email_input(self):
        self.email_input_image = PhotoImage(file="assets_login/input_bg.png")
        self.email_input_bg = Label(self.window, image=self.email_input_image, bg="#FFFFFF")
        self.email_input_bg.place(x=355, y=280)

        #input
        self.email_input = Entry(self.window, border=0,font=('', 14), width=23, bg=self.color, fg="white")
        self.email_input.place(x=375, y=294)
        self.email_input.insert(0, "Email")
    
    def create_password_input(self):
        self.password_input_image = PhotoImage(file="assets_login/input_bg.png")
        self.password_input_bg = Label(self.window, image=self.email_input_image, bg="#FFFFFF")
        self.password_input_bg.place(x=355, y=370)

        #input
        self.password_input = Entry(self.window, show="*",border=0,font=('', 14), width=23, bg=self.color, fg="white")
        self.password_input.place(x=375, y=384)
        self.password_input.insert(0, "*****")
    
    def create_button_login(self):
        self.button_login_img = PhotoImage(file="assets_login/button_bg.png")
        self.button_login = Button(self.window, image=self.button_login_img, border=0, activebackground="#FFFFFF", bg="#FFFFFF",command=lambda:threading.Thread(target=self.login).start())
        self.button_login.place(x=700,y=650)

    def create_message_error(self):
        self.message_regsiter = Label(self.window, text="Email já cadastrado ou Confirmação de senha invalida!", bg="#FFFFFF", fg="red")                
        self.message_regsiter.place(x=355, y=430)

    def create_logo(self):
        self.logo_image = PhotoImage(file="assets_login/logo.png")
        self.logo_login = Label(self.window, image=self.logo_image, bg="#FFFFFF")
        self.logo_login.place(x=385, y=100)
    
    def login(self):
        l = LoginUser()
        self.email = self.email_input.get()
        self.password = self.password_input.get()
        l.setData(f"{self.email}".lower(), f"{self.password}")
        if l.logged == True:
            l.logged = False
            HomeInterface(self.email)
        else:
            print("Data wrongs")
            self.create_message_error()
        
    def destroy(self):
        try:
            print("asd")
        except:
            pass

if __name__ == "__main__":
    LoginGUI()