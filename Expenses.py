#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import os

#Directory where the excel file is stored
os.chdir('/Users/parasbhandari/PycharmProjects')
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

#Now write into new xls file including totalexpense column
df.to_excel('total-expenses.xlsx', index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




