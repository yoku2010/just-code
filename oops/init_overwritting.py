#!/usr/bin/python

class Employee:
    def __init__(self):
        self.employee_name = 'John Mathew'
        print 'Employee __init__()'


class Manager:
    def __init__(self):
        self.manager_name = 'Alex Kellas'
        print 'Manager __init__()'


class HR(Employee, Manager):
    def __init__(self):
        Employee.__init__(self)
        Manager.__init__(self)
        self.hr_name = 'Scott'
        print 'HR __init__()'

class Company(HR):
    def __init__(self):
        HR.__init__(self)
        for cls in HR.__bases__:
            cls.__init__(self)
        self.company_name = 'Marutsakha'
        print 'Company __init__()'



# creating Employee class object
e = Employee()
print e.employee_name
print '\n'

# creating Manager class object
m = Manager()
print m.manager_name
print '\n'

# creating HR class object
h = HR()
print h.hr_name
print '\n'

# creating Company class object
c = Company()
print c.company_name
print (c.hr_name, c.employee_name, c.manager_name) # you can access other variables of parent classes
