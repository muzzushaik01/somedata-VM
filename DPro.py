import DPro1
class BonusError(Exception):
    pass
class ProjectError(Exception):
    pass

class Employee_Scheme:
    Bonus = 2
    Project = ['Python','Java', 'C']
    def __init__(self, Employee_Name, Sap_Id, Salary, MyProject ):
        self.Employee_Name = Employee_Name
        self.Sap_Id = Sap_Id
        self.Salary = Salary
        self.MyProject = MyProject

    def Employee_Details(self):
        print("Name = {}, Sap_Id = {}, Salary = {}, Project = {}".format(self.Employee_Name, self.Sap_Id, self.Salary, self.MyProject))
        Dpro1obj.Upload_Employee_ToDB(self.Employee_Name, self.Sap_Id, self.Salary, self.MyProject)
    def Update_Salary(self,AddToSalary):
        self.Salary += AddToSalary

    def Add_Bonus(self,HowMuchBonus):
        try:
            if(HowMuchBonus <= self.Bonus ):
                self.Salary *= HowMuchBonus
            else:
                raise BonusError
        except BonusError:
            print("BonusError : Bonus should be less than 200%")

    def Change_Project(self,ToWhichProject):
        try:
            if (ToWhichProject in self.Project):
                self.MyProject = ToWhichProject
                print(self.MyProject)
            else:
                raise ProjectError
        except ProjectError:
            print("ProjectError : Cannot change Project")

Nandu = Employee_Scheme("Nandamma", 52130534, 30000, "Java")
Dpro1obj = DPro1.EmployeeDB()
#Nandu.Employee_Details()
Dpro1obj.search_employee_inDB("Nandamma")
#Dpro1obj.update_salary("Nandamma",10000)
#Nandu.Update_Salary(int(input()))
#Nandu.Employee_Details()
#Nandu.Add_Bonus(2.5)
#Nandu.Change_Project("asdfg")
#Nandu.Employee_Details()


    #def Change_Project(self)



