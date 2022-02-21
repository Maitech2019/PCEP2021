#class dir isinstance (optional function)

#isinstance = check object within class
#dir => show attribute and method
#__class__=> show CLASS name of the OBJECT

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
obj2 = Employee("ian", 2000, "manager")
obj3 = Employee("ania", 2000, "sales")

print(isinstance(obj1, Employee))    #check if obj1 is created from class Employee()
                                    #if True/False
print(dir(obj1) #check method option of the object


print(obj1.__class__) #check what class the object from what class
                    #<class '__main__.Employee'>

