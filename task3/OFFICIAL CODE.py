# -*- coding: utf-8 -*-
"""
Edited on Thu Mar 24 16:09:19 2022

@author: adbz417
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read excel file and add names for the columns 
df = pd.read_excel(r'C:/Users/adbz417/Downloads/programming/Backup.xlsx', header=None, names=['Account', 'Postcodes','Latitude','Longitude','Men','Women','Children'])
#make the plot a square
plt.figure(figsize =(20,20))

#create a range to remove outlier values 
df =df[(df['Latitude']>49) & (df['Latitude']<61)]
print(df.columns)

fig = plt.figure()
print(df['Longitude'])
#size of the scatter graph
plt.figure(num=1,dpi=100)

#plot scatter graph for men and scale dot size
#change colour to red
plt.scatter(df['Longitude'],df['Latitude'],c='r',s=df['Men']/100)
#label the axis
plt.xlabel('Longitude')
plt.ylabel('Latitude')

#plot scatter graph for women and scale dot size
#change colour to green
plt.scatter(df['Longitude'],df['Latitude'],c='g',s=df['Women']/100)
#label the axis
plt.xlabel('Longitude')
plt.ylabel('Latitude')

#plot scatter graph for children and scale dot size
#change colour to blue 
plt.scatter(df['Longitude'],df['Latitude'],c='b',s=df['Children']/100)
#label the axis
plt.xlabel('Longitude')
plt.ylabel('Latitude')

#x = plt.axes()
x = np.arange(0,0.5,1)
y = np.arange(0,0.5,1)

#combine all graphs and add a title
plt.title('Scatter')
plt.show()
print(df.head())

#save file
plt.savefig("Final_scatter_plot.png")
