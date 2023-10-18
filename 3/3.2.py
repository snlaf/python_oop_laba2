class Employee:
    company = "Industries Co."
    status = None
    task = None

arthur = Employee
arthur.status = "Waiting"
arthur.task = "Programming"
arthur.salary = 3400
arthur.name = "Arthur"
arthur.age = 25

print(f'Работник компании {arthur.company} решил выполнить своё задание "{arthur.task}", но сейчас он {arthur.status}. Ему {arthur.age} лет, его зовут {arthur.name} и он получает {arthur.salary} долларов в месяц')