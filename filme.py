class movie:
    free = []
    busy = []
    rooms = []
    movies = []
    prices = []
    seat = []
    busy_seat = []
    all_user_seat = []

    def __init__(self):
        self.name = "name"
        self.duration = "duration"
        self.price = float()
        
    def busy_room(self):
        pass
    
    def read_json(self):
        import json
        with open("room.json", 'r') as f:
            data = json.load(f)
        return data
    
    def write_json_busy(self, room, edit):
        import json
        data = self.read_json()
        data[room]["ocupado"] = edit
        with open('room.json', 'w') as f:
            json.dump(data, f)
    
    def write_json_name(self, room, edit):
        import json
        data = self.read_json()
        data[room]["movie"] = edit
        with open('room.json', 'w') as f:
            json.dump(data, f)

    def write_json_price(self, room, edit):
        import json
        data = self.read_json()
        data[room]["preco"] = edit
        with open('room.json', 'w') as f:
            json.dump(data, f)

    def write_json_busy_seat(self, room, id, edit):
        import json
        data = self.read_json()
        data[room]["lugares_ocupados"].insert(id, edit)
        with open('room.json', 'w') as f:
            json.dump(data, f)


    def verify_room(self):
        import json
        free = movie.free
        busy = movie.busy
        path = self.read_json()
        for r in path:
            if path[r]['ocupado'] == "" :
                if not r in free:
                    free.append(r)
            elif not r in busy:
                    busy.append(r)
        try:
            self.write_json_busy(free[0], 'x')
            self.write_json_name(free[0], self.name)
            self.write_json_price(free[0], self.price)
            busy.append(free[0])
            free.pop(0)
            print(free)
            print(busy)
        except:
            print(f"Todas as salas estão ocupadas!\nSalas ocupadas: {busy}\nSalas Livres: {free}")
    
    def update_room(self):
        import json
        free = movie.free
        busy = movie.busy
        path = self.read_json()
        for r in path:
            if path[r]['ocupado'] == "":
                if not r in free:
                    free.append(r)
            elif not r in busy:
                    busy.append(r)
    
    def getAllRoom(self):
        rooms = movie.rooms
        for i in self.read_json():
            rooms.append(i)
        return rooms

    def getAllMovies(self):
        movies = movie.movies
        r = self.read_json()
        for i in r:
            movies.append(r[i]['movie'])
        return movies
    
    def getAllPrices(self):
        prices = movie.prices
        r = self.read_json()
        for i in r:
            prices.append(r[i]['preco'])
        return prices
    
    def getAllSeat(self):
        seats = movie.seat
        r = self.read_json()
        for i in r:
            seats.append(r[i]["lugares"])
        return seats
    
    def getAllBusySeat(self):
        busy_seat = movie.busy_seat
        r = self.read_json()
        for i in r:
            busy_seat.append(r[i]["lugares_ocupados"])
        return busy_seat

    def setData(self, name, duration, price):
        self.name = name
        self.duration = duration
        self.price = price
        self.verify_room()

    
m = movie()