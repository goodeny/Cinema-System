from filme import movie
from register import UserRegistration
class PainelAdmin:
    def __init__(self):
        self.m = movie()
        self.r = UserRegistration()

        """
        print(f"Room busy: {self.show_room_busy()}")
        print(f"Room free: {self.show_room_free()}")
        print(f"All rooms: {self.all_room()}")
        print(f"All movies: {self.m.getAllMovies()}")
        """

        #self.unbusy_all()
        #print(f"All seats: {self.m.getAllSeat()}")
        #print(f"All Busy seat: {self.m.getAllBusySeat()}")
        #print(f"All user registrated: {self.all_users()}")

    def addMovie(self, name, duration, price):
        self.m.setData(name, duration, price)
    
    def show_room_busy(self):
        self.m.update_room()
        return self.m.busy
    
    def show_room_free(self):
        self.m.update_room()
        return self.m.free
    
    def all_room(self):
        return self.m.getAllRoom()

    def unbusy_all(self):
        for i in self.m.read_json():
            self.m.write_json_busy(i, "")
            self.m.write_json_name(i, "")

    def all_users(self):
        return self.r.read_client_json()

    def getUser(self, id):
        for i in self.all_users():
            if i[0] == id:
                return i
    
    def getSeat(self, id):
        return self.getUser(id)[6]
    
    def edit_busy_seat(self):
        m = movie()
        m.write_json_busy_seat("sala1", 0, "fechado")
    
    def add_json_user_seat(self, id_user, assento):
        import json
        data = self.all_users()
        for i in data:
            if i[0] == id_user:
                i[6].append(f"{assento}")
                with open('client.json', 'w') as f:
                    json.dump(data, f)
    
    def modify_bank(self, id_user, qnt):
        import json
        data = self.all_users()
        for i in data:
            if i[0] == id_user:
                i[7] = qnt
                with open ('client.json', 'w') as f:
                    json.dump(data, f)
    
    def remove_json_user_seat(self, id_user, a):
        import json
        data = self.all_users()
        for i in data:
            if i[0] == id_user:
                i[6].pop(a)
                with open('client.json', 'w') as f:
                    json.dump(data, f)
        
    def clear_json_user_seat(self, id_user):
        import json
        data = self.all_users()
        for i in data:
            if i[0] == id_user:
                i[6].clear()
                with open('client.json', 'w') as f:
                    json.dump(data, f)

    """def write_json_busy_seat(self, room, id, edit):
        import json
        data = self.read_json()
        data[room]["lugares_ocupados"].insert(id, edit)
        with open('room.json', 'w') as f:
            json.dump(data, f)"""
        
move = PainelAdmin()

#move.remove_json_user_seat(2, 1)
#print(move.getSeat(2))
#move.remove_json_user_seat(2,3)
#move.clear_json_user_seat(2)
#move.edit_busy_seat()
#move.getSeat(1)
#nome do filme, a duração, e o preço do ingresso
#move.addMovie("Test", "3 Minutos", 200)
#move.unbusy_all()





    
    

    