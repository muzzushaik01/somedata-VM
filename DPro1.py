import pyodbc
server = 'HCL-02-76\SQLEXPRESS01'
database = 'Employee1'
username = 'Muzammil'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class EmployeeDB:
        def Show_Employees_inDB(self):

            for Emps in Emp:
                print("Employee Name: {}, SapID : {}, Salary: {}, Project: {}".format(Emps.NameOfEmployee,Emps.SapID,Emps.Salary,Emps.Project))

        def Upload_Employee_ToDB(self,NameOfEmployee,SapID,Salary,Project):
            print("Call received")
            query = '''  
                            INSERT INTO Employee_table(NameOfEmployee,SapID,Salary,Project)
                            VALUES
                            ('{0}',{1},{2},'{3}')  '''


            insertQuery = query.format(NameOfEmployee,SapID,Salary,Project)
            print(insertQuery)
            cursor.execute(insertQuery)
            cnxn.commit()
            print("Employee committed to DB")

        def search_employee_inDB(self,employee):
            query = ''' select * from Employee_table where NameOfEmployee = '{0}' '''
            searchQuery = query.format(employee)
            values = cursor.execute(searchQuery)
            print("employee is in db")
            flag = 1
            for Emp in values:
                print("EmployeeName:{} , EmployeeSalary:{}".format(Emp.NameOfEmployee,Emp.Salary))
                flag = 0
            if(flag == 0):
                self.update_salary(employee)

        def update_salary(self,employee):
            #print(SalaryHike)
            try:
                query = ''' select * from Employee_table where NameOfEmployee= '{0}' '''
                searchQuery = query.format(employee)
                values = cursor.execute(searchQuery)
                for Emp in values:
                    employeesalary = Emp.Salary
                    #print(employeesalary)
                    EmplQuery = ''' 
                                Update Employee_table SET Salary = {0} WHERE NameOfEmployee = '{1}'
                                '''
                    updateQuery = EmplQuery.format(employeesalary+100000, employee)
                    print(updateQuery)
                    cursor.execute(updateQuery)
                    # commits data to DB
                    cursor.commit()
                    print("Updated salary")
            except:
                pass













