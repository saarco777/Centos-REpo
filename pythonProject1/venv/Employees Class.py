"""
how to get the user email adress
"""

class employees:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

emp1 = employees('Gal', 'Cohen', 30000)
emp2 = employees('Liran', 'Cohen', 40000)
emp3 = employees('Saar', 'Cohen', 50000)
emp4 = employees('Yossi', 'Cohen', 60000)

print(emp1.first + 's', 'pay is', emp1.pay)
print('If you want to contact', emp1.first, ', his email address is:', emp1.email, end='\n\n')

#print(emp.first + 's', 'pay is', pay)  # emp2 pay info
print('If you want to contact', emp2.first, ', his email address is:', emp2.email, end='\n\n')  # emp2 email address

#print(emp3.first + 's', 'pay is', pay)  # emp3 pay info
print('If you want to contact', emp3.first, ', his email address is:', emp3.email, end='\n\n')  # emp3 email address

#print(emp4.first + 's', 'pay is', pay)  # emp4 pay info
print('If you want to contact', emp4.first, ', his email address is:', emp4.email,)  # emp4 email address


