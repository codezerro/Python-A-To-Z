class Employee:
    def employeeDetails(self):
        self.name="kabir"
        print("Name = ",self.name)
        self.age =23
        print("age = ",self.age)

    def printEmployeeDetails(self):
        print("printing from print employee details method")
        print("Name = ",self.name)
        print("Age = ",self.age)


employee=Employee()
employee.employeeDetails()
employee.printEmployeeDetails()


#Employee.employeeDetails(employee)