class Employee:
    company = "Industries Co."
    status = None
    task = None

arthur = Employee
arthur.salary = 3600
arthur.name = "Arthur"

edwin = Employee
edwin.salary = 3600
edwin.name = "Edwin"

print(arthur.salary + edwin.salary)