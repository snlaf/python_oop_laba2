class Employee:
    company = "Industries Co."
    status = None
    task = None
    def test_show(self, name, salary):
        return name + ' ' + salary


arthur = Employee
arthur.salary = 3600
arthur.name = "Arthur"

print(arthur.name, arthur.salary)