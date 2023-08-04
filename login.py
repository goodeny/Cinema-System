from register import UserRegistration

class LoginUser:
    def __init__(self):
        self.email = "".lower()
        self.password = ""
        self.logged = False
        
    def verify_login(self):
        self.registration = UserRegistration()
        if self.email in self.registration.get_all_email():
            for i in self.registration.read_client_json():
                if self.password == i[4]:
                    self.logged = True
        else:
            return print("Password or Email incorrect!")
        
    def setData(self, email, password):
        self.email = email
        self.password = password
        self.verify_login()


