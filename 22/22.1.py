class Validator:

    def __init__(self):
        pass

    def isEmail(self, str):
        return ('@' in str) and ('.' in str)

    def isPhone(self, str):
        import re
        phone = re.match(r'\+7\ \([0-9]{3}\)\ [0-9]{3}-[0-9]{2}-[0-9]{2}', str)
        return phone is not None


    def isDomain(self, domain):
        return ('.' in domain)




email = "example@example.com"
phone_number = "+7-123-456-78-90"
dom = "01-01-2022"

validator = Validator()

if validator.isEmail(email):
    print("Email адрес валиден")
else:
    print("Email адрес невалиден")

if validator.isPhone(phone_number):
    print("Номер телефона валиден")
else:
    print("Номер телефона невалиден")

if validator.isEmail(email):
    print("Адрес валиден")
else:
    print("Адрес невалиден")