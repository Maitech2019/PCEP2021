#name, salary

class Employee:
    #method
    def detail(self,empname,empsalary,empdepartment):
        self.name = empname
        self.salary = empsalary
        self.department = empdepartment
        print("name = {}".format(self.name))
        print("salary = {}".format(self.salary))
        print("department = {}".format(self.department))

    


#object

obj1 = Employee()
obj1.detail("May", 3000, "account")

obj2 = Employee()
obj2.detail("Aten", 3000, "programmer")

obj3 = Employee()
obj3.detail("JO", 4000, "lawyer")
