class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def full_name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, employee_id):
        Person.__init__(self, first, last)
        self.employee_id = employee_id

    def employee_name(self):
        return self.full_name() + ", " +  str(self.employee_id)
