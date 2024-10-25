#!/usr/bin/env python
# coding: utf-8

# In[32]:


"""All codes written below are regarding DATA SCIENCE ADVANCED. """
"""All codes written below are regarding DATA SCIENCE LINEAR REGRESSION."""


import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
full_health_data = pd.read_csv("data.csv",header=0,sep=",")
x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie_Burnage"]
slope,intercept,r,p,std_err = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc,x))
plt.scatter(x,y)
plt.plot(x,slope * x + intercept)
plt.ylim(ymin=0,ymax=2000)
plt.xlim(xmin=0,xmax=200)
plt.xlabel("Average_Pulse")
plt.ylabel("Calorie_Burnage")
plt.show()

"""All codes regarding LINEAR REGRESSION are completed here."""


# In[54]:


"""All codes written below are regarding REGRESSION TABLE."""


import pandas as pd
import statsmodels.formula.api as smf
full_health_data = pd.read_csv("data.csv",header=0,sep=",")
model = smf.ols('Calorie_Burnage ~ Average_Pulse',data = full_health_data)
results = model.fit()
print(results.summary())

"""All codes regarding REGRESSION TABLE are completed here."""


# In[58]:


"""All codes written below are regarding REGRESSION TABLE COEFFICIENTS."""


def pcb(Average_Pulse):
    return(0.3296*Average_Pulse + 346.8662)
print(pcb(120))
print(pcb(130))
print(pcb(150))
print(pcb(180))

"""All codes regarding REGRESSION TABLE COEFFICIENTS are completed here."""


# In[64]:


"""All codes written below are regarding REGRESSION TABLE: R-SQUARED."""


import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
full_health_data = pd.read_csv("data.csv",header=0,sep=",")
x = full_health_data["Duration"]
y = full_health_data["Calorie_Burnage"]
slope,intercept,r,p,std_err = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc,x))
print(mymodel)
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.ylim(ymin=0,ymax=2000)
plt.xlim(xmin=0,xmax=200)
plt.xlabel("Duration")
plt.ylabel("Calorie_Burnage")
plt.show()

"""All codes regarding REGRESSION TABLE: R-SQUARED are completed here."""


# In[74]:


"""All codes written below are regarding LINEAR REGRESSION CASE."""


import pandas as pd
import matplotlib.pyplot as plt
full_health_data = pd.read_csv("data.csv",header=0,sep=",")
model = smf.ols("Calorie_Burnage ~ Average_Pulse + Duration",data = full_health_data)
results = model.fit()
print(results.summary())

def pcb(Average_Pulse,Duration):
    return(3.1695*Average_Pulse + 5.8434 * Duration - 334.5194)
print(pcb(110,60))
print(pcb(140,45))
print(pcb(175,20))

"""All codes regarding LINEAR REGRESSION CASE are completed here."""
"""All codes regarding DATA SCIENCE ADVANCED are completed here."""


# In[ ]:




