class Employee:
    company = "Industries Co."
    status = None
    task = None
    def test_show(self):
        print(self.name)


arthur = Employee()
arthur.salary = 3600
arthur.name = "Arthur"

arthur.test_show()