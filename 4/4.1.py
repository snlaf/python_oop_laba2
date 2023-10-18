class Employee:
    company = "Industries Co."
    status = None
    task = None

arthur = Employee

Edwin = Employee

print(f'Работник компании {arthur.company} решил выполнить своё задание "{arthur.task}", но сейчас он {arthur.status}. Ему {arthur.age} лет, его зовут {arthur.name} и он получает {arthur.salary} долларов в месяц')