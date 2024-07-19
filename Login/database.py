import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = {}
        self.load()
    
    def load(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    email, password, name, created = line.strip().split(";")
                    self.users[email] = (password, name, created)
        except FileNotFoundError:
            # Se o arquivo não existir, inicializa um dicionário vazio
            self.users = {}
    
    def get_user(self, email):
        return self.users.get(email, -1)
    
    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email already exists")
            return -1
    
    def validate(self, email, password):
        user_data = self.get_user(email)
        if user_data != -1:
            return user_data[0] == password
        else:
            return False
    
    def save(self):
        with open(self.filename, "w") as file:
            for email, (password, name, created) in self.users.items():
                file.write(f"{email};{password};{name};{created}\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
