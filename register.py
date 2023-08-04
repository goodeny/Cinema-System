class UserRegistration:
    def __init__(self):
        self.email = "".lower()
        self.name = "".lower()
        self.second_name = "".lower()
        self.password = ""
        self.password_confirm = ""
        self.registred = False
    
    def register_user(self):
        if not self.email in self.get_all_email():
            if self.password == self.password_confirm:
                import json
                data = self.read_client_json()
                data.append([0, self.email, self.name, self.second_name, self.password, "", [], 13200])
                self.registred = True
                with open('client.json', 'w') as f:
                    json.dump(data, f)

                self.update_id()
                print("Data saved and updated id!")
            else:
                print("Password don't match")
        else:
            print("Email already registred!")

    def read_client_json(self):
        import json
        with open("client.json", "r") as f:
            data = json.load(f)
        return data
    
    def update_id(self):
        id = 0
        import json
        data = self.read_client_json()
        for i in data: 
            id += 1
            i[0] = id
            with open('client.json', 'w') as f:
                json.dump(data, f)
        print("id updated")

    def get_all_email(self):
        list_email = []
        data = self.read_client_json()
        for i in data:
            list_email.append(i[1])
        return list_email
    
    def setData(self, email, name, second_name, password, password_confirm):
        self.email = email
        self.name = name
        self.second_name = second_name
        self.password = password
        self.password_confirm = password_confirm
        self.register_user()