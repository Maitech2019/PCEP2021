
#encapsulate

class Employee:
    def __init__(self,empname,empsalary,empdepartment): #to set initial attribute (constructor)

        #protected attribute
        self._name = empname
        self._salary = empsalary
        self._department = empdepartment
        self_showData()###########public and protected METHOD can be called from inside CLASS##
        
        print("name = {}".format(self._name))
        print("salary = {}".format(self._salary))
        print("department = {}".format(self._department))

        ################protected Method
    def _showData(self):
        print("name = {}".format(self._name))
        print("salary = {}".format(self._salary))
        print("Employed = {}".format(self._department))

obj1 = Employee("may", 2000, "sales")
obj1._name = "Jan"   #change attribute using protected ._name

obj2 = Employee("drew", 2000, "programmmer")
obj2.name = "Matt"   #change attribut using public .name (python accept,and pass\
                     #but will not change the attribute!

print(obj1._name) #name now is Jan
print(obj2._name) #name still drew



