# Object constructor & Destructor

# Destructor # is a defalt method (option)when end class
# def __del__(self):
# pass

# constructor # is a defalt method (option)when start class
# def __init__(self):
# pass


#name, salary

class Employee:
    #def __init__ (self):
        #print("Defalt instructor")

    def __init__(self,empname,empsalary,empdepartment): #to set initial attribute (constructor)
        self.name = empname
        self.salary = empsalary
        self.department = empdepartment
        
        print("name = {}".format(self.name))
        print("salary = {}".format(self.salary))
        print("department = {}".format(self.department))

    def showData(self):
        print("Employed = {}".format(self.department))

    def __del__(self):
        print("Call Destructor")
        
#object

obj1 = Employee("may", 1000, "sales")
obj1.name = "methinee"  # change attribute before encapsulate
obj1.salary = 2000
obj1.showData()

obj2 = Employee("ian", 2000, "manager")

obj3 = Employee("ania", 2000, "sales")
