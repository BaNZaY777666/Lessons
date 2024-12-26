class House:
    def __init__(self, name, floor_number):
        self.name = name
        self.floor_number = floor_number

    def say_info(self):
        print(f'Название дома {self.name}, колличество этажей {self.floor_number}')

    def __len__(self):
        return self.floor_number

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floor_number}'

    def __eq__(self, other):
        return self.floor_number == other.floor_number

    def __lt__(self, other):
        return self.floor_number < other.floor_number

    def __le__(self, other):
        return self.floor_number <= other.floor_number

    def __gt__(self, other):
        return self.floor_number > other.floor_number

    def __ge__(self, other):
        return self.floor_number >= other.floor_number

    def __ne__(self, other):
        return self.floor_number != other.floor_number

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.floor_number + value)
        elif isinstance(value, House):
            return House(self.name, self.floor_number + value.floor_number)

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floor_number:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 +10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
