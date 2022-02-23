#class variable & instance variable
#class variable = global variable, static variable

class Employee:
    #class variable = don't need obj(can call directly in public and proteced only)
    _minSalary = 12000
    _maxSalary = 50000
    _companyname = "xyz"

    def __init__(self,name,salary,department): #constructor

        #instant variable ("object variable"= need to create object to get attribute)
        #private attribute
        self.__name = name
        self.__salary = salary
        self._department = department

        #proteced method
    def _showData(self):
        print("My name = "+self.__name)
        print("salary = ",format(self.__salary))
        print("job = "+self._department)

################CALL INSTANT VARIABLE
obj1 = Employee("Drew",300000,"accounting")
obj1._showData()
print(obj1._department)

################CALL CLASS VARIABLE
print(Employee._minSalary)
print("Minimum salary: ", str(Employee._minSalary))
print("Max Salary: ",Employee._maxSalary)

#print(Employee._department)#CANNOT access because need to creat object: object variable
print(Employee._companyname)
#print(Employee.__companyname)#CANNOT access when set in PRIVATE VARIABLE
