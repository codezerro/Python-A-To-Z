class Employee:
    def setNumberOfWorkingHours(self):
        self.setNumberOfWorkingHours = 40

    def DisplayNumberOfWorkingHours(self):
        print(self.setNumberOfWorkingHours)


class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.setNumberOfWorkingHours = 44

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()


employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee : ", end=' ')
employee.DisplayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of Trainee : ", end=' ')
trainee.DisplayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print("After reset the number of working hours : ", end=' ')
trainee.DisplayNumberOfWorkingHours()
