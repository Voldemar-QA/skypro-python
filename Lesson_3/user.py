class User:

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.lastName = last_name

    def sayName(self):
        print("Моё имя:", self.name)

    def sayLastName(self):
        print("Моя фамилия:", self.lastName)

    def sayFullName(self):
        print("Моё полное имя:", self.name, self.lastName)
