class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name)

arthur = Employee('Arthur', 3600)
arthur.show()