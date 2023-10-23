class Student:
    place = "school"
    name = None
    surname = None

    def show(self, string):
        if len(string) > 0:
            return string[0].upper() + string[1:]
        else:
            return string

alex = Student()
alex.name = 'Alex'
alex.surname = 'Schmidt'

print(alex.show(alex.name))