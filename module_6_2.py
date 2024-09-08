class Vehicle:
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    __COLOR_VARIANTS = ['blue', 'red', 'white', 'black']

    def get_model(self):
        return print(f"Модель: {self.__model}")

    def get_horsepower(self):
        return print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        return print(f"Цвет: {self.__color}")

    def print_info(self):
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f'Владелиц: {self.owner}')
        return

    def set_color(self, new_color):
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя поменять цвет на {new_color}')

class Sedan(Vehicle):
    def __PASSENGERS_LIMIT(self):
        self.limit = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()