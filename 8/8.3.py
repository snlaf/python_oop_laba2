class Student:
    place = "school"
    name = None
    surname = None

    def show(self, first_name, last_name):
        initials = first_name[0].upper() + last_name[0].upper()
        return initials

alex = Student()
alex.name = 'Alex'
alex.surname = 'Schmidt'

print(alex.show(alex.name, alex.surname))