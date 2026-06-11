class Employee:
    # pass -- use pass when the class need not be used or defined right now
    def __init__(self,first,last,pay):      # __init__ is the constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    #Methods 
    def fullname(self):
        return self.first + " " + self.last

emp1 = Employee("Akhil","Nair",35000)
emp2 = Employee("Alan","Siju",40000)
print(emp1.email, emp2.email)

#Following both are same
print(Employee.fullname(emp1))
print(emp1.fullname()) 





#The following is required when there is no constructor and is not an ideal process
# emp1 = Employee()
# emp2 = Employee()
# emp1.first = "Alan"
# emp1.last = "Siju"
# emp1.email = "Alan.Siju@company.com"
# emp1.pay = 40000

# emp2.first = "Alin"
# emp2.last = "Saiju"
# emp2.email = "Alin.Saiju@company.com"
# emp2.pay = 50000
