from admin import PainelAdmin
from filme import movie
from tkinter import *
import threading


class PageConfirm:
    def __init__(self, user_info):
        self.admin = PainelAdmin()
        self.user_info = user_info
        self.id = 0
        self.sala = ""
        self.name = ""
        self.seat = []
        self.bank = 0
        self.price = 0
        self.name_movie = ""

        for i in self.user_info:
            self.name = i[5][0]
            self.id = i[0][0]
            self.sala = i[2][0]
            self.name_movie = i[3][0]
        print(self.sala)
        #self.confirm(self.sala)
        self.bank = self.admin.getUser(self.id)[7]
        self.price_total(self.sala)
        print("Meu saldo: ", self.bank)
        print("preço total: ", self.price)
        self.getSeats()
        print(self.seat)
        self.create_interface()
    
    def confirm(self, room):
        self.m = movie()
        import json
        data = self.m.read_json()
        for i in self.admin.getUser(self.id)[6]:
            if not i in data[room]["lugares_ocupados"]:
                data[room]["lugares_ocupados"].insert(-1, i)
                with open('room.json', 'w') as f:
                    json.dump(data, f)
            print("já foi adicionado")
    
    def getSeats(self):
        for i in self.admin.getUser(self.id)[6]:
            self.seat.append(f'A{i}')
    
    def price_total(self, room):
        count = 0
        self.m = movie()
        import json
        data = self.m.read_json()
        self.price = len(self.admin.getUser(self.id)[6]) * data[room]["preco"]
        
    def create_interface(self):
        self.window = Tk()
        self.window.geometry("1000x768")
        self.window.resizable(0,0)
        self.window.title("Cinema Bey")
        self.window.config(bg="#45438C")
        self.create_note()
        self.create_header()
        self.button_finish()

        self.window.mainloop()

    def create_header(self):
        self.header = Label(self.window,bg='#FFFFFF', height=5)
        self.header.pack(fill='x')

        self.title = Label(self.header, text=f"Pagamento", font="'', 16", fg="black",bg="white")
        self.title.place(x=435, y=24)

    def create_note(self):
        self.note_name = Label(self.window, text=f"Nome: {self.name.capitalize()}\n\nNome do filme: {self.name_movie}\n\nAssento: {self.seat}\n\nPreço total: {self.price}", font="'',16", bg="#45438C")
        self.note_name.place(x=100, y=100)
        self.saldo = Label(self.window, text=f"Saldo: {self.bank}", font="'',16", bg="#45438C")
        self.saldo.place(x=800, y=100)
    
    def button_finish(self):
        self.button_img = PhotoImage(file="assets_confirm/button.png")
        self.create_button_finish = Button(self.window, text="Finalizar", bg="white", border=0,fg="black", command=lambda:threading.Thread(target=self.verify_saldo()).start())
        self.create_button_finish.place(x=760, y=650)

    def verify_saldo(self):
        if self.bank >= self.price:
            self.admin.modify_bank(self.id, (self.bank-self.price))
            self.message_error = Label(self.window, text="Compra realizada com sucesso! Ingresso comprado", bg="#45438C", fg="white", font="'',20")
            self.message_error.place(x=300,y=655)
            self.confirm(self.sala)
        else:
            self.message_error = Label(self.window, text="Saldo insuficiente! Transação Cancelada", bg="#45438C", fg="white", font="'',20")
            self.message_error.place(x=300,y=655)
            admin = PainelAdmin()
            admin.clear_json_user_seat(self.id)