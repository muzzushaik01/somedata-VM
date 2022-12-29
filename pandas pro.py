import pandas as pd
'''
df = pd.read_csv('pokemon_data.csv')
#to read data
#print(df)
#to read whole data in the file
#print(df.to_string())
#to print top 5 lines in the fu
#print(df.head())
#to print the required column
print(df['Name'].to_string)

#to print the index and row using the for loop

for index, row in df.iterrows():
    print(index,row)
    print(index, row['Name'])

de = pd.read_csv('pokemon_data.csv')
print(de)
de.loc[de["Type 1"] == "Grass"]

# to add a new column
de['Total'] = de['HP'] + de['Attack'] + de['Defense']
print(de.to_string())
#own_try

for index, row['Type 1'] in de.iterrows():
    if(de[row['Type 1'] == 'NaN']):
        de.fillna('Muzzu')
print(index, row['Type 1'])
'''




#to drop a column or delete a colu
#to fill the empty values

dv = pd.read_excel('pokemon_data.xlsx')
print(dv.to_string())
dvv = dv.fillna('NullMuzz')
print(dvv.to_string())

ee = dv.groupby(['Type 1'])
#print(ee.group_keys())
print(ee.groups) # it is printing all the groups
print(ee.get_group("Grass")) #it is printing
print(ee.all('Grass'))

print(ee.indices) # return indexes

dv.groupby(pd.Grouper(key="Type 1")).count()

dv.groupby(pd.Grouper(key="Type 1")).cumcount()

dv.groupby(pd.Grouper(key="Type 1")).mean()

dv.groupby(pd.Grouper(key="Type 1")).max()

dv.groupby(pd.Grouper(key="Type 1")).min()

dv.groupby(pd.Grouper(key="Type 1")).median()

dv.groupby(pd.Grouper(key="Type 1")).cummax()

dv.groupby(pd.Grouper(key="Type 1")).cummin()
#dv.groupby('Type 2').cumcount()

print(ee.squeeze)


#

