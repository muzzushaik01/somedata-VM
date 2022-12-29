import unittest
import UploadFiles
import filelocation
import pyodbc

server = 'HCL-02-18\SQLEXPRESS'
database = 'FileSearchResults'
username = 'vyshu'
password = 'Vyshu@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class test_capstone(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass
    def test_upload_file_results_todb(self):
        uploadObj = UploadFiles.UploadFilesToDB()
        #fileObj = filelocation.FindFileLocation()
        uploadObj.upload_file_results_todb("dummytestcasefile.txt","C:\\Users\\user697\\PycharmProjects\\pythonProject\\testdata\\dummy\\dummytestcasefile.txt",0)
        #uploadObj.upload_file_results_todb("test.txt","C:\\Users\\user697\\PycharmProjects\\pythonProject\\testdata\\test.txt", 0)

        values_1 = cursor.execute(''' select * from FileSearchResults_table where NameOfFile = 'dummytestcasefile.txt' ''')

        #values_2 = cursor.execute(''' select * from FileSearchResults_table where NameOfFile = 'test.txt' ''')
        for fileInfo in values_1:

            self.assertEqual(fileInfo.NameOfFile, "dummytestcasefile.txt")
            self.assertEqual(fileInfo.File_Location, "C:\\Users\\user697\\PycharmProjects\\pythonProject\\testdata\\dummy\\dummytestcasefile.txt")
