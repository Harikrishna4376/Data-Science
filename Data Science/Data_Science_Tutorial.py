#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Checking the length of each list in the dataset
for key, value in data.items():
    print(f"{key}: {len(value)}")


# In[45]:


import pandas as pd

# Create the data as a dictionary
data = {
    "Duration": [30, 30, 45, 45, 45, 60, 60, 60, 75, 75],
    "Average_Pulse": [80, 85, 90, 95, 100, 105, 110, 115, 120, 125],
    "Max_Pulse": [120, 120, 130, 130, 140, 140, 145, 145, 150, 150],
    "Calorie_Burnage": [240, 250, 260, 270, 280, 290, 300, 310, 320, 330],
    "Hours_Work": [10, 10, 8, 8, 0, 7, 7, 8, 0, 8],
    "Hours_Sleep": [7, 7, 7, 7, 7, 8, 8, 8, 8, 8]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('data2.csv', index=False)

print("CSV file 'data2.csv' created successfully.")


# In[33]:


"""All codes written below are regarding DATA_SCIENCE. """
"""All codes written below are regarding DATA SCIENCE TUTORIAL."""


import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
full_health_data = pd.read_csv("data.csv",header=0,sep=",")
x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie_Burnage"]
slope,intercept,r,p,std_err = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc,x))
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.ylim(ymin=0,ymax=2000)
plt.xlim(xmin=0,xmax=200)
plt.xlabel("Average_Pulse")
plt.ylabel("Calorie_Burnage")
plt.show()


# In[35]:


array = [80,85,90,95,100,105,110,115,120,125]
print(array)


# In[43]:


"""All codes written below are regarding PYTHON DATAFRAME."""


import pandas as pd
d = {'col1':[1,2,3,4,7],'col2':[4,5,6,9,5],'col3':[7,8,12,1,11]}
df = pd.DataFrame(data=d)
print(df)

count_column = df.shape[1]
print(count_column) #It will count the number of columns.

count_row = df.shape[1]
print(count_row) #It will count the number of rows.

"""All codes regarding PYTHON DATAFRAME are completed here."""


# In[55]:


"""All codes written below are regarding DATA SCIENCE FUNCTIONS."""


average_pulse_max = max(80,85,90,95,100,105,110,115,120,125)
print(average_pulse_max)  #It will display the max value.

average_pulse_min = min(80,85,90,95,100,105,110,115,120,125)
print(average_pulse_min)

import numpy as np
Calorie_burnage = [240,250,260,270,280,290,300,310,320,330]
Average_calorie_burnage = np.mean(Calorie_burnage)
print(Average_calorie_burnage) #calculates mean of all values.

"""All codes regarding DATA SCIENCE FUNCTIONS are completed here."""


# In[1]:


"""All codes written below are regarding DATA SCIENCE PREPARATION."""


import pandas as pd
health_data = pd.read_csv("data3.csv",header=0,sep=",")
print(health_data)

import pandas as pd
health_data = pd.read_csv("data3.csv",header=0,sep=",")
print(health_data.head()) #only displaying top 5 layers of the table.

health_data.dropna(axis = 0,inplace=True)
print(health_data) #it will drop all the blank rows.

print(health_data.info())

health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)
print(health_data.info()) #this code will convert entre data into float.

print(health_data.head())

print(health_data.describe()) #It will open the data entirely.

"""All codes regarding DATA SCIENCE PREPARATION are completed here."""
"""All codes regarding DATA SCIENCE TUTORIAL are completed here."""


# In[ ]:




