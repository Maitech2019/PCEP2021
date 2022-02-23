#getter setter method

class Employee:
    def __init__(self,empname,empsalary,empdepartment): #to set initial attribute (constructor)

        #private attribute (only allow CLASS EMPLOYEE CALL)
        self.__name = empname
        self.__salary = empsalary  ###Private __salary , no body can change salary
        self.__department = empdepartment ###Private __department, no body can change department

        
        #private Method (only allow CLASS EMPLOYEE CALL)
    def _showData(self): #only be called by class, not outside object
        print("name = {}".format(self.__name))
        print("salary = {}".format(self.__salary))
        print("Employed = {}"+ self.getDepartment()) #from get method 

    #setter method

    def setName(self,newname):
        self.__name = newname

    def setSalary(self,newsalary):
        self.__salary = newsalary

    def setDepartment(self,newdepartment):
        self.__department = newdepartment

    #getter method(instead of calling an attribue of class)

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department
    

###############
obj1 = Employee("may", 2000, "sales") #need to create obj first, to call get method on CLASS attribute
print(obj1.getName())
print(obj1.getSalary())
print("My department is ", obj1.getDepartment())

###############USE SETTER TO CHANGE PRIVATE ADDTIBUTE

obj1 = Employee("may", 2000, "sales")

obj1.setName("ping")
obj1.setSalary(5000)
obj1.setDepartment("programmer")

print(obj1.getName())
###############
obj1._name = "jan"        ##CAN chnage in (Protected mode) .__name
obj1.__salary = 4000      #CAN NOT change (#Private mode) .__salary
obj1.__department = "HR"  #CAN NOT change (#Private mode) .__department

obj1._showData()
