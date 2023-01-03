# # Part 1

# In[ ]:


import pandas as pd

Orders_xlsx = pd.read_excel("orders.xlsx")
df = pd.DataFrame(Orders_xlsx)
df.head()


# In[ ]:


data = []

# always inserting new rows at the first position - last row will be always on top  

data.insert(0, {'CO-1': 'CO-1', 'CITY68': 'CITY68', 1: 1})

# Concatanating original dataframe with additional row of data from list

pd.concat([pd.DataFrame(data), df], ignore_index=True) # does not save changes to the original dataframe

# Saving modified df as df2

df2 = pd.concat([pd.DataFrame(data), df], ignore_index=True)

df2.head()


# In[ ]:


catalogue_xlsx = pd.read_excel ('catalogue.xlsx')
df_catalogue = pd.DataFrame(catalogue_xlsx)
df_catalogue.head()


# In[ ]:


data_catalogue = []

# always inserting new rows at the first position - last row will be always on top  

data_catalogue.insert(0, {'CITY1': 'CITY1', 'Adult': 'Adult', 10.99: 10.99})

# Concatanating original dataframe with additional row of data from list

pd.concat([pd.DataFrame(data_catalogue), df_catalogue], ignore_index=True) # does not save changes to the original dataframe

# Saving modified df as df2

df_catalogue = pd.concat([pd.DataFrame(data_catalogue), df_catalogue], ignore_index=True)

df_catalogue.head()


# In[ ]:


print("all rows of order names is")
OrderNames = df2.iloc[:,0]
OrderNames.head()


# In[ ]:


print("all rows of Item names is")
od2=df2.iloc[:,1]
od2.head()


# In[ ]:


len(OrderNames)


# a

# In[ ]:



# In[ ]:

# dataframe Name and Age columns

import XlsxWriter

df3 = pd.DataFrame({'OrderNumbers': OrderNames,
                    'Item_numbers':[0]*34956,
                    'price X quantity':[0]*34956,
                    'Item_type':[0]*34956,
                    'Order_Number':[0]*34956
                    })

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('OrderValue.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df3.to_excel(writer, sheet_name='Sheet', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()


# In[ ]:


reader = pd.read_excel('OrderValue.xlsx')
df_OrderValue = pd.DataFrame(reader)
df_OrderValue.head()


# b

# In[ ]:


test = True
order_number = 0
current_row = 1


# c, d-j
# 

# In[ ]:


while test:
  for current_row_index in range(df2.iloc[:,0].size-1):
    
    if df2.iloc[:,0][df2.iloc[:,0].index[current_row_index+1]] == 'END': #1
     test = False
    
    else:

      item_number = df2.iloc[:,1][df2.iloc[:,1].index[current_row_index]] #2
      item_number = int(item_number.replace('CITY', ''))
      df_OrderValue.at[current_row_index, 'Item_numbers'] = item_number

      #3
      item_price = df_catalogue.iloc[item_number-1,2]
      part_value = item_price * df2.iloc[current_row_index,2]
      df_OrderValue.at[current_row_index, 'price X quantity'] = part_value

      gender = df_catalogue.iloc[item_number-1,1]
      df_OrderValue.loc[current_row_index, 'Item_type'] = gender
      

      if pd.isna(df2.iloc[current_row_index,0]) != True:
        order_number+=1
      df_OrderValue.at[current_row_index, 'Order_Number'] = order_number
      
    
  break

 
print(test)


# In[ ]:


df_OrderValue.head()


# In[ ]:


df_minimized = df_OrderValue.loc[df_OrderValue['Order_Number'] == 2802]
print(df_minimized)
minimized = ['Man','Woman','Child']
j=0
df_minimized = df_minimized.loc[df_minimized['Item_type'] == minimized[j]]
df_minimized['total_value'] = df_minimized['price X quantity'].sum()
print(df_minimized)

    
    
  
  
  


# In[ ]:


subsetDataFrame = df_OrderValue[(df_OrderValue['Order_Number'] == 6580) & (df_OrderValue['Item_type'] == 'Woman') ]
subsetDataFrame['total_value'] = subsetDataFrame['price X quantity'].sum()
subsetDataFrame


# In[ ]:


writer_2 = pd.ExcelWriter('OrderValue.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df_OrderValue.to_excel(writer_2, sheet_name='Sheet', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer_2.save()


# # Part 2

# In[ ]:


import pandas as pd

master_xlsx = pd.read_excel ('master.xlsx')
df_master = pd.DataFrame(master_xlsx)

df_master.head()


# In[ ]:


data_master = []

# always inserting new rows at the first position - last row will be always on top  

data_master.insert(0, {'A': 27454, 6580:6580,	2802:2802,	8789:8789,	3943:3943,	6944:6944,	9270:9270,	9787:9787})

# Concatanating original dataframe with additional row of data from list

pd.concat([pd.DataFrame(data_master), df_master], ignore_index=True) # does not save changes to the original dataframe

# Saving modified df as df2

df_master_2 = pd.concat([pd.DataFrame(data_master), df_master], ignore_index=True)

master_index_value = 27454
for master_index in range(0,1000):
  df_master_2.at[master_index, 'A'] = master_index_value
  master_index_value+=1

df_master_2


# In[ ]:


df_master_2.iloc[0,:][df_master_2.iloc[0,:].index[1+1]]


# In[ ]:


Account_Numbers = df_master_2.iloc[:,0]
print(Account_Numbers)


# In[ ]:


# dataframe Name and Age columns
df_master_3 = pd.DataFrame({'Account_Numbers': Account_Numbers,
                    'Men':[0]*1000,
                    'women':[0]*1000,
                    'children':[0]*1000
                    
                    })

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer_master_3 = pd.ExcelWriter('AccountValue.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df_master_3.to_excel(writer_master_3, sheet_name='Sheet', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer_master_3.save()


# In[ ]:


reader_master_3 = pd.read_excel('AccountValue.xlsx')
df_AccountValue = pd.DataFrame(reader_master_3)
df_AccountValue.head()


# In[ ]:


test_2 = True
Man_Value = 0
Woman_Value = 0
Child_Value = 0
genders = ['Man','Woman','Child']


# In[ ]:


while test_2:
  for current_row_index in range(df_AccountValue.iloc[:,0].size-1):
    total_account_value_man = 0
    total_account_value_woman = 0
    total_account_value_child = 0

    for current_column_index in range(1,22):
      if pd.isna(df_master_2.iloc[current_row_index,:][df_master_2.iloc[0,:].index[current_column_index]]) != True:
        order_in_account= df_master_2.iloc[current_row_index,:][df_master_2.iloc[0,:].index[current_column_index]]
        
        for item in genders:
          if item == 'Man':
            subsetDataFrame = df_OrderValue[(df_OrderValue['Order_Number'] == order_in_account) & (df_OrderValue['Item_type'] == 'Man') ]
            subsetDataFrame['total_value'] = subsetDataFrame['price X quantity'].sum()
            try:
             total_account_value_man += int(subsetDataFrame.iloc[0,:][subsetDataFrame.iloc[0,:].index[5]])
            except IndexError:
              pass
            
            df_AccountValue.at[current_row_index, 'Men'] = total_account_value_man
            
          elif item == 'Woman':
            subsetDataFrame = df_OrderValue[(df_OrderValue['Order_Number'] == order_in_account) & (df_OrderValue['Item_type'] == 'Woman') ]
            subsetDataFrame['total_value'] = subsetDataFrame['price X quantity'].sum()
            try:
             total_account_value_woman += int(subsetDataFrame.iloc[0,:][subsetDataFrame.iloc[0,:].index[5]])
            except IndexError:
              pass
            df_AccountValue.at[current_row_index, 'women'] = total_account_value_woman
            
          elif item == 'Child':
            subsetDataFrame = df_OrderValue[(df_OrderValue['Order_Number'] == order_in_account) & (df_OrderValue['Item_type'] == 'Child') ]
            subsetDataFrame['total_value'] = subsetDataFrame['price X quantity'].sum()
            try:
             total_account_value_child += int(subsetDataFrame.iloc[0,:][subsetDataFrame.iloc[0,:].index[5]])
            except IndexError:
              pass
            df_AccountValue.at[current_row_index, 'children'] = total_account_value_child
           
        
    
  break
    

 
print(test)


# In[ ]:


df_AccountValue.head()


# In[ ]:


writer_4 = pd.ExcelWriter('AccountValue.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df_AccountValue.to_excel(writer_4, sheet_name='Sheet', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer_4.save()


# 

# 
