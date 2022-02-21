#encapsulate

class Employee:
    def __init__(self,empname,empsalary,empdepartment): #to set initial attribute (constructor)

        #private attribute (only allow CLASS EMPLOYEE CALL)
        self._name = empname
        self.__salary = empsalary  ###Private __salary , no body can change salary
        self.__department = empdepartment ###Private __department, no body can change department

        self.__showData() #private method,so only CLASS EMPLOYEE can call

        
        #private Method
    def __showData(self): #only CLASS EMPLOYEE can call/use this private mode __
        print("name = {}".format(self._name))
        print("salary = {}".format(self.__salary))
        print("Employed = {}".format(self.__department))

###############

obj1 = Employee("may", 2000, "sales")

###############
obj1._name = "jan"
##CAN change in (Protected mode) ._name
#if change def _showdata to (public or protect mode)and call
#obj1._showData() in (public or protect mode)

###############

obj1.__salary = 4000
#CAN NOT change (#Private mode) .__salary
obj1.__department = "HR"
#CAN NOT change (#Private mode) .__department

obj1.__showData()
##CAN NOT call outside class becoz it's (#Private Method) only Class can call

