
#it is a function used for analysing, cleaning, exploring and manipulating data
#panda refers to panel data and python data analysis
#panda allows us to analyze big data and make conclusions, help to clean messy data sets, make them readable and relavent

# series --
# dataframe --



import pandas as pd
'''
mydataset = {'bikes':["honda","splender","scooty"], 'meilage':[40,50,35]}
mydata =pd.DataFrame(mydataset)
#we can also change the index values
#Inder_change = pd.DataFrame(mydataset, index = ['b1','b2','b3'])
#print(Inder_change)
#print(Inder_change.loc['b2'])

print(mydata)
print(mydata.loc[0])

#print(mydata.loc[[0,1]])
#loc - locate is used to print only required things : compare the above two for more understanding

#to check the version of the pandas we can use __version__
print(pd.__version__)

#using pandas Series is used to print the data in column type one by one,[one dimensional array] and it also defines the dtype
a = [1,6,5]
series = pd.Series(a)
print(series)
HAPPY = pd.Series(a, index = [10,20,30])
print(HAPPY) #Lables - it can be used to access a specified value, similiar to our indexes


#we can also locate rows in DataFrames
'''
#comma seperated files
df=pd.read_csv('Data1.txt')
print(df)
#read_csv is used to read the custom document
#read_json is similar csv , json is mainly used when the data is vey big
#to_string is used to print the entire data
#head() function is used to get the topdata of the document
#if we give head() then the 1st five data elements will print automatically
#tail() is opposite to head()
#info() gives more information about the dataset
#non null value indicates there is no value presents, not a 0

print(df.head(2))
print(df.tail(2))
print(df.info())
'''
#we can know the system's maximum rows
print(pd.options.display.max_rows)

#we can also modify the rows 
pd.options.display.max_rows = 999
'''
mu = pd.read_csv('Data2.txt')
#print(mu.to_string())

#Cleaning data
#removing empty cells
#to remove empty cell we use a function called dropna()
#the dropna() method returns a new DataFrame, and will not change the original
#muz = mu.dropna()
#print(muz.to_string())
#to change the original DataFrame, use the inplace = True argument
#mu.dropna(inplace = True)
#print(mu.to_string())
#to fill the null values we use fillna() arguement











