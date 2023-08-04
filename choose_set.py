from admin import PainelAdmin
from page_confirm import PageConfirm
from filme import movie
from tkinter import *

class seat:
    def __init__(self, w, h, pos_x, pos_y, color, seat_id, seat_busy, seat_free, u_id, window, complete):
        self.complete = complete
        self.window = window
        self.u_id = u_id
        self.seat_id = seat_id
        self.seat_busy = seat_busy
        self.seat_free = seat_free
        self.w = w
        self.h = h
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.busy = []

    def create_seat(self,t):
        self.seat = Button(self.window, text=t, bg=self.color, width=self.w, height=self.h, border=0, command=lambda:self.busy_seat())
        self.seat.place(x=self.pos_x, y=self.pos_y)

    def busy_seat(self):
        self.list = []
        if not self.seat_id in self.seat_busy:
            if not self.seat_id in self.busy:
                self.bt_img = PhotoImage(file="assets_choose/bt.png")
                self.button_choose = Button(self.window, text="Proximo", width=10,height=2, border=0, command=lambda:self.page_confirm())
                self.button_choose.place(x=750,y=670) 
                self.seat.config(bg="red")
                self.busy.append(self.seat_id)
                admin = PainelAdmin()
                admin.add_json_user_seat(self.u_id,self.seat_id+1)
                
                print(self.seat_id)
                for i in self.busy:
                    print(i)
            else:
                self.button_choose.destroy()
                self.seat.config(bg="#05FF00")
                admin = PainelAdmin()
                admin.remove_json_user_seat(self.u_id,self.seat_id)
                self.busy.remove(self.seat_id)
                print("removeu")
        else:
            print(f"já está selecionado {self.seat_id}")

    def page_confirm(self):
        PageConfirm(self.complete)
    
class UserChooseSeat:
    def __init__(self, user_info):
        self.color = "#45438C"
        self.user_info = user_info
        print(self.user_info)
        self.user_id = user_info[0]
        self.room_id = user_info[1]
        self.room_name = user_info[2]
        self.movie_name = user_info[3]
        self.movie_price = user_info[4]
        self.name = user_info[5]
        self.complete = []
        self.complete.append([[self.user_id],[self.room_id],[self.room_name],[self.movie_name],[self.movie_price],[self.name]])
        m = movie()
        self.s = m.getAllSeat()[self.room_id]
        self.b = m.getAllBusySeat()[self.room_id]
        self.create_interface()
    
    def create_interface(self):
        self.window = Tk()
        self.window.geometry("1000x768")
        self.window.resizable(0,0)
        self.window.title("Cinema Bey")
        self.window.config(bg=self.color)
        self.create_header()
        self.create_seat()
        self.create_screen()
        self.window.mainloop()

    def create_header(self):
        self.header = Label(self.window,bg='#FFFFFF', height=5)
        self.header.pack(fill='x')

        self.title = Label(self.header, text=f"{self.name}, Escolha o seu assento!", font="'', 16", fg="black",bg="white")
        self.title.place(x=330, y=24)

    def create_screen(self):
        self.screen_choose = Label(self.window, text='TELA',width=120,height=2)
        self.screen_choose.place(x=90, y=520)

    def create_button(self):
        self.bt_img = PhotoImage(file="assets_choose/bt.png")
        self.button_choose = Button(self.window, text="Proximo", width=10,height=2, border=0)
        self.button_choose.place(x=750,y=670) 

    def create_seat(self):
        self.busy_id = []
        self.free_id = []
        if self.b == []:
            for i in range(6):
                self.free_id.append(i)
                c = seat(4,2, (i+2.3)*100, 300, "#05FF00",  i,self.busy_id, self.free_id, self.user_id,self.window, self.complete)
                c.create_seat(f"A{i+1}")
        elif len(self.b) > 0:
            for i in range(6):
                if self.s[i] in self.b:
                    self.busy_id.append(i)
                    c = seat(4,2, (i+2.3)*100, 300, "red", i, self.busy_id, self.free_id, self.user_id, self.window, self.complete)
                    c.create_seat(f"A{i+1}")
                                
                elif not self.s[i] in self.b:
                    self.free_id.append(i)
                    c = seat(4,2, (i+2.3)*100, 300, "#05FF00",  i,self.busy_id, self.free_id, self.user_id,self.window, self.complete)
                    c.create_seat(f"A{i+1}")
    def a():
        pass
