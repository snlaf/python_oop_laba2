class Car:
    color = None
    fuel = None
    company = 'Toyota'
    model = 'Sprinter Trueno APEX (AE 86)'
    def show_stat(self):
        print(f'Автомобиль марки {car1.company}, модель {car1.model}, цвета "{car1.color}", с предположительным баков в {car1.fuel} литров двигалась вниз по склону. Будьте осторожны')

car1 = Car()
car1.fuel = 75
car1.color = "Panda"

car1.show_stat()