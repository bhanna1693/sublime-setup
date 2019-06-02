
import sys
print(sys.executable)
print(sys.version)


class Employee:
    """A sample Employee class"""
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)


for num in [1, 2, 3, 4]:
    print(num)

emp_1 = Employee('John', 'Smith', 57000)

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
