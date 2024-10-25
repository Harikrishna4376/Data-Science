#!/usr/bin/env python
# coding: utf-8

# In[11]:


"""All codes written below are regarding DATA SCIENCE STATISTICS. """
"""All codes written below are regarding INTRO TO STATISTICS. """


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
full_health_data = pd.read_csv("data2.csv",header=0,sep=",")
print(full_health_data.describe())

"""All codes regarding INTRO TO STATISTICS are completed here."""


# In[37]:


"""All codes written below are regarding STATISTICS PERCENTILES."""


import numpy as np
Max_Pulse = full_health_data["Max_Pulse"]
percentile10 = np.percentile(Max_Pulse,10)
print(percentile10)

"""All codes regarding STATISTICS PERCENTILES are completed here."""


# In[43]:


"""All codes written below are regarding STATISTICS STANDARD DEVIATION."""


import numpy as np
std = np.std(full_health_data)
print(std) #Prints the standard deviation of "data2.csv".

import numpy as np
cv = np.std(full_health_data) / np.mean(full_health_data)
print(cv) #prints CV as std deviation divided by mean.

"""All codes regarding STATISTICS STANDARD DEVIATION are completed here."""


# In[73]:


"""All codes written below are regarding STATISTICS VARIANCE."""


import numpy as np
import pandas as pd
health_data = pd.read_csv("data2.csv",header=0,sep=",")
var = np.var(health_data)
print(var)

import pandas as pd
import numpy as np
full_health_data = pd.read_csv("data.csv",header=0,sep=",")
var_full = np.var(full_health_data)
print(var_full) #calculating var for "data.csv".

"""All codes regarding STATISTICS VARIANCE are completed here."""


# In[101]:


"""All codes written below are regarding STATISTICS CORRELATION."""


import matplotlib.pyplot as plt
health_data.plot(x = 'Average_Pulse',y='Calorie_Burnage',kind='scatter')
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
negative_corr = {'Hours_Work_Before_Training':[10,9,8,7,6,5,4,3,2,1],'Calorie_Burnage':[220,240,260,280,300,320,340,360,380,400]}
negative_corr = pd.DataFrame(data=negative_corr)
negative_corr.plot(x = 'Hours_Work_Before_Training',y = 'Calorie_Burnage',kind='scatter')
plt.show() #negative plot of original plot.

import matplotlib.pyplot as plt
full_health_data.plot(x = 'Duration',y = 'Max_Pulse',kind ='scatter')
plt.show()

"""All codes regarding STATISTICS CORRELATION are completed here."""


# In[151]:


"""All codes written below are regarding STATISTICS CORRELARION MATRIX."""


Corr_Matrix = round(full_health_data.corr(),2)
print(Corr_Matrix) #round() is used to display output of 2 decimals.

import matplotlib.pyplot as plt
import seaborn as sns
correlation_full_health = full_health_data.corr()
axis_corr = sns.heatmap(
    correlation_full_health,
    vmin=-1,vmax=1,center=0,
    cmap = sns.diverging_palette(5000,5000,n=5000),
    square=True
)
plt.show() #numbers like 5000,n=5000 will force the code to show 5000 colors.

"""All codes regarding STATISTICS CORRELATION MATRIX is completed here."""


# In[8]:


"""All codes written below are regarding STATISTICS CORRELATION 
VS CAUSALITY."""


import matplotlib.pyplot as plt
import pandas as pd
drowning_accident = [20,40,60,80,100,120,140,160,180,200]
ice_cream_sale = [20,40,60,80,100,120,140,160,180,200]
drowning = {"drowning_accident":
           [20,40,60,80,100,120,140,160,180,200],
           "ice_cream_sale":[20,40,60,80,100,120,140,160,180,200]}
drowning = pd.DataFrame(data=drowning)
drowning.plot(x="ice_cream_sale",y="drowning_accident",kind="scatter")
plt.show()
correlation_beach = drowning.corr()
print(correlation_beach)

"""All codes regarding STATISTICS CORRELATION VS CAUSALITY are 
completed here."""
"""All codes regarding DATA SCIENCE STATISTICS are completed here."""


# In[ ]:




