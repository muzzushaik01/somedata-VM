import pyodbc
server = 'HCL-02-76\SQLEXPRESS01'
database = 'Employeee'
username = 'Muzammil'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Employee_scheme:


    def Table_Creation(self):
        try:

            values = cursor.execute(''' select * from Employee_table ''')
            query1 = cursor.execute(''' use Employeee ''')
            query2 = cursor.execute(''' create table Employeee_table(
                                    NameOfEmp varchar(100),
                                    Emp_Id int NOT NULL,
                                    Salary int,
                                    Project varchar(100)
                                    PRIMARY KEY(Emp_Id))
                                    ''')
            cnxn.commit()
        except:
            print("Table is already present")

Object = Employee_scheme()
Object.Table_Creation()