import pandas as pd
import os

#Directory where the excel file is stored
os.chdir('/<yourdirectorypath>')
fileName = 'expenses.xlsx'

#Read excel file into data frame
df = pd.read_excel(fileName, header=1)
print(df)

#We only want to add expense1, expense2, expense3 columns. so make the columns list removing first column employeeid
col_to_add = list(df)
col_to_add.remove('employeeid')
print(col_to_add)

#sum each row of data frame using sum fuction 
df['totalexpense'] = df[col_to_add].sum(axis=1)
print(df)

#Now write into new csv file including totalexpense column
df.to_csv('total-expenses.csv', index=False)
