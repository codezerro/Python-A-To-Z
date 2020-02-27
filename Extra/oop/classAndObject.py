class Employee:
    name = "Shariar Kabir"
    designation = "Sales Executive"
    saleMadeThisWeek = 6
    def hasAchievedTarget(self):
        if self.saleMadeThisWeek >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")

employeeOne = Employee()
print(employeeOne.name)
print(employeeOne.hasAchievedTarget())

number = {1,2,3,4}
ty=type(number)
print(ty)