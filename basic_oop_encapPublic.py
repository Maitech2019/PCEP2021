#encapsulation  = <method+variable>= class
# only allows owner to change class: method/attribute

#Access Modifier = access to Class, Attribute, Method
#Public = anybody can access and call
#Protected(_) = only use (_) only access "class" and "child class"
#Private(__) = use (__) only access to certain class
#######################################################
#encapsulation
class Employee:
    def __init__(self,empname,empsalary,empdepartment): #to set initial attribute (constructor)

        #public attribute
        self.name = empname
        self.salary = empsalary
        self.department = empdepartment
        
        print("name = {}".format(self.name))
        print("salary = {}".format(self.salary))
        print("department = {}".format(self.department))

    #public Method
    def showData(self):
        print("Employed = {}".format(self.department))

    def __del__(self):
        print("Call Destructor")
        
#object

obj1 = Employee("may", 1000, "sales")
obj1.name = "jan"   #anybody can change attribute
obj1.salary = 500000 #anybody can change attribute

obj2 = Employee("ian", 2000, "manager")
obj3 = Employee("ania", 2000, "sales")










