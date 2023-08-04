from filme import movie
from register import UserRegistration
from choose_set import UserChooseSeat
from admin import PainelAdmin
from tkinter import *
import threading

class UserSelected:
    def __init__(self, id, u_id, u_name):
        m = movie()
        self.user_name = u_name
        self.user_id = u_id
        self.room_id_selected = id
        self.room_name = m.getAllRoom()[self.room_id_selected]
        self.movie_name = m.getAllMovies()[self.room_id_selected]
        self.price_value = m.getAllPrices()[self.room_id_selected]
        self.complete = [self.user_id, self.room_id_selected, self.room_name, self.movie_name, self.price_value, self.user_name]

class Card:
    def __init__(self, window):
        self.window = window
    
    def create_card(self, t, h, w, x, y, id, u_id, u_name):
        self.user_name = u_name
        self.user_id = u_id
        self.card = Button(self.window, text=t, height=h, width=w, command=lambda:self.user_select_room(id))
        self.card.place(x=x, y=y)

    def user_select_room(self, id):
        u = UserSelected(id, self.user_id, self.user_name)
        u.room_id_selected = id
        if u.movie_name != "":
            #print(u.price_value)
            UserChooseSeat(u.complete)
        else:
            return print("Nenhum filme")

class HomeInterface:
    def __init__(self, email):
        self.id = 0
        self.email = email
        self.name = ""
        self.datauser = []
        self.id_sala = 0
        self.getID()
        admin = PainelAdmin()
        admin.clear_json_user_seat(self.id)
        self.create_interface()

    def getID(self):
        r = UserRegistration()
        for i in r.read_client_json():
            if self.email == i[1]:
                self.datauser.append(i)
                self.id = i[0]
                self.name = i[2]
                print(self.id)
                print(self.name)
    
    def create_interface(self):
        self.window = Tk()
        self.window.title("Cinema Bey")
        self.window.resizable(0,0)
        self.window.geometry("1000x768")
        self.window.config(bg="#45438C")

        self.create_header()
        self.create_content()

        self.window.mainloop()

    def create_header(self):
        self.header = Label(self.window,bg='#FFFFFF', height=5)
        self.header.pack(fill='x')

        self.title = Label(self.header, text=f"Olá {self.name.capitalize()}, seja bem vindo ao Cinema Bey!", font="'', 16", fg="black",bg="white")
        self.title.place(x=300, y=24)

    def create_content(self):
        self.content = Label(self.window, height=150, bg="#4F61A3")
        self.content.pack(fill='both', pady=170)
        c = Card(self.content)
        for i in range(5):
            f = self.add_filmes_content(i)
            self.id_sala = i
            c.create_card(f"{f}",15, 20, (i+0.3)*180, 50, i, self.id, self.name)
    
    def add_filmes_content(self, x):
        m = movie()
        f = m.getAllMovies()[x]
        if f == "":
            f = "Vazio"
            return f
        else:
            return f

