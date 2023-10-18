class Car:
    color = None
    fuel = None
    company = 'Toyota'
    model = 'Sprinter Trueno APEX (AE 86)'

    def go(self):
        pass

    def turn(self):
        pass

    def stop(self):
        pass

    def show_stat(self):
        print(f'Автомобиль марки {Car.company}, модель {Car.model}, цвета "{Car.color}", с предположительным баков в {Car.fuel} литров двигалась вниз по склону. Будьте осторожны')
