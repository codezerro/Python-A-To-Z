class Employee:
    def employeeDetails(self):
        self.name = "kabir"
    @staticmethod
    def welcomeMessage():
        print("welcome to python learning world")


employee=Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()