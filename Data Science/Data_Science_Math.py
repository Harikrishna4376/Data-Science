#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""All codes written below are regarding DATA SCIENCE MATH."""

"""All codes written below are regarding DATA SCIENCE PLOTTING
LINEAR FUNCTIONS. """


import matplotlib.pyplot as plt
import pandas as pd
import sys
health_data = pd.read_csv("data2.csv",header=0,sep=",")
health_data.plot(x = 'Average_Pulse',y = 'Calorie_Burnage',kind='line'),
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.show()

"""All codes regarding DATA SCIENCE PLOTTING LINEAR FUNCTIONS
are completed here."""


# In[17]:


"""All cpdes written below are regarding SLOPE AND INTERCEPT."""


def slope(x1,y1,x2,y2):
    s = (y2-y1)/(x2-x1)
    return s
print(slope(80,240,90,260)) #This code will calculate slope.

import pandas as pd
import numpy as np
health_data = pd.read_csv("data2.csv",header=0,sep=",")
x = health_data["Average_Pulse"]
y = health_data["Calorie_Burnage"]
slope_intercept = np.polyfit(x,y,1)
print(slope_intercept)

def myfunc(x):
    return 2*x + 80
print(myfunc(135))

import matplotlib.pyplot as plt
health_data.plot(x = 'Average_Pulse',y = 'Calorie_Burnage',kind = 'line'),
plt.ylim(ymin=0,ymax=400)
plt.xlim(xmin=0,xmax=150)
plt.show()

"""All codes regarding DATA SCIENCE SLOPE AND INTERCEPT are completed here."""
"""All codes regarding DATA SCIENCE MATH are completed here."""


# In[ ]:




