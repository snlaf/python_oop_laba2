class Employee:
    company = "Industries Co."
    status = None
    task = None

arthur = Employee
arthur.status = "Waiting"
arthur.task = "Programming"

print(f'Работник компании {arthur.company} решил выполнить своё задание "{arthur.task}", но сейчас он {arthur.status}')