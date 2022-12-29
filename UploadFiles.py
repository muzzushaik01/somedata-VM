import pyodbc

server = 'HCL-02-76\SQLEXPRESS01'
database = 'FileSearchResults'
username = 'Muzammil'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class UploadFilesToDB:

    def show_file_search_results_fromdb(self):
        values = cursor.execute('select * from FileSearchResults_table')
        for fileInfo in values:
            print("File Name: {}".format(fileInfo.NameOfFile))
            print("File Location: {}".format(fileInfo.File_Location))

    def upload_file_results_todb(self,fileName, fileLocation, searchCount):
        query = '''  
                    INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                    VALUES
                    ('{0}',{1},'{2}')  '''

        insertQuery = query.format(fileLocation, searchCount, fileName)
        cursor.execute(insertQuery)
        cnxn.commit()
        print("New file search results committed to DB")

    # searches for a file in db
    # Input : Filename (string)
    # output : True or False (Boolean)
    def search_in_db_for_file(self, fileName):
        # select query
        query = ''' select * from FileSearchResults_table where NameOfFile = '{0}' '''
        searchQuery = query.format(fileName)
        values = cursor.execute(searchQuery)
        flag=0
        for fileInfo in values:
            print("==========================")
            print("File name: {}".format(fileInfo.NameOfFile))
            print("File path: {}".format(fileInfo.File_Location))
            print("==========================")
            flag=1
        if (flag == 0):
            return True
            self.update_file_searchcount(fileName)
        else:
            return False



    def update_file_searchcount(self, fileName):
        query = ''' select * from FileSearchResults_table where NameOfFile = '{0}' '''
        searchQuery = query.format(fileName)


        values = cursor.execute(searchQuery)

        for fileInfo in values:
            fileSearchCount = fileInfo.SearchCount
            fileinfoQuery = '''
                    Update FileSearchResults_table SET SearchCount = {0} WHERE NameOfFile = '{1}'
                    '''
            updateQuery = fileinfoQuery.format(fileSearchCount + 1, fileName)
            cursor.execute(updateQuery)
            cursor.commit()
            print("Updated file search count")

a = UploadFilesToDB()
#a.show_file_search_results_fromdb()
#a.upload_file_results_todb("himuz", "nofile/jff/himuz.txt", 0)
#a.show_file_search_results_fromdb()
a.search_in_db_for_file("himuz")
