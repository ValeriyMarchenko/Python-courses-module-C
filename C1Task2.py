class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Balance: {self.balance} rubles'

    def get_info(self):
        return f'{self.name} {self.surname} lives in {self.city} '

guest_1 = Client('Ivan', 'Petrov', 'Moscow', 50)
guest_2 = Client('Nastya', 'Marchenko', 'Minsk', 500)
guest_3 = Client('Petya', 'Ivanov', 'Novosibirsk', 150)

guest_list = [guest_1, guest_2, guest_3]

for guest in guest_list:
    print(guest.get_info())