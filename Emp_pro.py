import DataB
import pyodbc
server = 'HCL-02-76\SQLEXPRESS01'
database = 'Employeee'
username = 'Muzammil'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class ProjectError(Exception):
    pass
class ProjectChangeError(Exception):
    pass

class BonusError(Exception):
    pass

class IdError(Exception):
    pass


class Employee:
    project=['python','c','java']
    bonus=2
    def __init__(self,NameOfEmp,Emp_Id,Salary,Project):
        self.NameOfEmp=NameOfEmp
        self.Emp_Id=Emp_Id
        self.Salary=Salary
        self.Project=Project
    def tablecreation(self):
        createobj.Table_Creation()
    def insert_Employeee_Details(self):
        query='''  
                    INSERT INTO Employeee_table (NameOfEmp,Emp_Id,Salary,Project)
                    VALUES
                    ('{0}',{1},{2},'{3}')  '''
        insert_query=query.format(self.NameOfEmp,self.Emp_Id,self.Salary,self.Project)
        cursor.execute(insert_query)
        cnxn.commit()
        print("Employee details entered into the DataBase")

    def View_Employee_Details(self):

        query='''select * from Employeee_table where NameOfEmp = '{0}' '''
        searchquery=query.format(self.NameOfEmp)
        values=cursor.execute(searchquery)
        for Emp in values:
            print("Employee details from DB")
            print("Name Of employee={}".format(Emp.NameOfEmp))
            print("Emp_Id={}".format(Emp.Emp_Id))
            print("Salary={}".format(Emp.Salary))
            print("Project={}".format(Emp.Project))

    def add_bonus(self):
        try:
            bonus=int(input())
            if(0<bonus<2):
                query = ''' select * from Employeee_table where NameOfEmp='{}' '''
                searchquery = query.format(self.NameOfEmp)
                values = cursor.execute(searchquery)
                for Info in values:
                    print(Info)
                    oldsalary = Info.Salary
                    newsalary = oldsalary * (1 + bonus)
                    print(newsalary)
                    query1 = ''' UPDATE Employeee_table SET Salary={0} WHERE NameOfEmp='{1}' '''
                    query2 = query1.format(newsalary, self.NameOfEmp)
                    # print(query2)
                    cursor.execute(query2)
                    # print(query2)
                    cnxn.commit()
            else:
                raise BonusError
        except BonusError:
            print("bonus should not be less than 0 and more than 2")

        except:
            pass
    def update_salary(self):
        try:
            new_salary = int(input())
            query = ''' select * from Employeee_table where NameOfEmp='{}' '''
            searchquery = query.format(self.NameOfEmp)
            values = cursor.execute(searchquery)
            for Info in values:
                oldsalary = Info.Salary
                query = '''UPDATE Employeee_table SET Salary={0} WHERE NameOfEmp='{1}' '''
                query1 = query.format(new_salary, self.NameOfEmp)
                cursor.execute(query1)
                cnxn.commit()
        except:
            pass

    def change_project(self):
        new_project = input()
        try:
            query = '''select * from Employeee_table where NameOfEmp='{0}' '''
            searchquery = query.format(self.NameOfEmp)
            values = cursor.execute(searchquery)
            for fileinfo in values:
                oldproject = fileinfo.Project
                if new_project == oldproject:
                    raise ProjectChangeError
                elif (new_project not in self.project):
                    raise ProjectError
                else:
                    query = '''UPDATE Employeee_table SET Project='{0}' WHERE NameOfEmp='{1}' '''
                    query1 = query.format(new_project, self.NameOfEmp)
                    cursor.execute(query1)
                    cnxn.commit()
                    print("congrats ,your in new project")
        except ProjectError:
            print("No similar Project Available")
        except ProjectChangeError:
            print("You cant change to same Project")

        except:
            pass

    def delete_Emp_details(self):
        try:
            Which_Employee= int(input())
            query = '''select * from Employeee_table'''
            values = cursor.execute(query)
            Id_list= []
            for info in values:
                Id_list.append(info.Emp_Id)
                if Which_Employee in Id_list:
                    query = '''delete from Employeee_table where Emp_Id={} '''
                    query1 = query.format(Which_Employee)
                    cursor.execute(query1)
                    cnxn.commit()
                else:
                    raise IdError
        except IdError:
            print("Emp_Id is not found in the DB")
        except:
            pass

createobj=DataB.Employee_scheme()
obj=Employee("Nandamma",520,350000,"python")
obj.insert_Employeee_Details()
#obj.delete_Emp_details()
#obj.Display_Emp_Details()
#obj.add_bonus()
#obj.update_salary()
#obj.change_project()