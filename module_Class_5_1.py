

class House:
    def __init__(self, name, floor_number):
        self.name = name
        self.floor_number = floor_number

    def say_info(self):
        print(f'Название дома {self.name}, колличество этажей {self.floor_number}')


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floor_number:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# h1.say_info()
# h2.say_info()

h1.go_to(5)
h2.go_to(10)

