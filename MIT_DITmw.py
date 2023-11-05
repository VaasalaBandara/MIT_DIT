#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
#importing the csv file FOR MIT
df=pd.read_csv("/home/vaasala/Desktop/extra_coding/heart_rate/MIT3.csv")


# In[9]:


#printing the csv file
print(df)


# In[10]:


import pandas as pd
#importing the csv file for DIT
df2=pd.read_csv("/home/vaasala/Desktop/extra_coding/heart_rate/DIT1.csv")


# In[11]:


print(df2)


# In[12]:


#visualizing the columns MIT
df.head(6)


# In[13]:


#visualizing columns DIT
df2.head(6)


# The sample sizes of each appear to be large.The sample variances are unknown and independent samples. Therefore the standard normal distribution suffices 

# # BREAST_HEART

# In[14]:


#the heart absorption for breast of MIT
x1=df["breast_Heart(%)"]
x1=x1.dropna()
print(x1)


# In[68]:


#heart absorption from breast for DIT
x2=df2["breast_Heart(%)"]
x2=x2.dropna()
print(x2)


# In[70]:


#mean values
import statistics as stat
m1=stat.mean(x1)
print(m1)
m2=stat.mean(x2)
print(m2)


# In[41]:


#to check whether the populations are normally distributed
from scipy import stats
st1,p_x1=stats.shapiro(x1) #shapiro test for x1 population
st2,p_x2=stats.shapiro(x2)#shapiro test for x2 population


# In[42]:


#test of siginificance of shapiro test p-values
print(p_x1)
print(p_x2)
if p_x1 and p_x2<0.05:
    print("they are not from normal distributions")
else:
    print("they are from normal distributions")


# since the p-value of both are extremely lower than the rejection reigon, we will reject the null hypothesis. The data is not derived from a normal distribtuion

# The Mann-Whitney U test is a better option since the populations are not normals

# In[32]:


#mann_whitney U test for the variables
from scipy import stats
st,p1=stats.mannwhitneyu(x1,x2,alternative='greater')
print(p1)


# In[34]:


#considering 0.05 level of significance
if p1<0.05:
    print("reject null hypothesis")
    print("MIT is more effective than DIT")
elif p1>0.05:
    print("accept null hypothesis")
    print("DIT is more effective than MIT")
else:
    print("not applicable")


# # BREAST_LEFTLUNG

# In[37]:


#left lung rate from breast for MIT
x3=df["breast_Lung(%)"]
x3=x3.dropna()
print(x3)


# In[71]:


#left lung rate for breast for DIT
x4=df2["breast_Lung(%)"]
x4=x4.dropna()
print(x4)


# In[72]:


#mean values
import statistics as stat
m3=stat.mean(x3)
print(m3)
m4=stat.mean(x4)
print(m4)


# In[44]:


#shapiro test to check if populations are normal
from scipy import stats
st1,p_x3=stats.shapiro(x3)#shapiro test for x3 population
st2,p_x4=stats.shapiro(x4)#shapiro test for x4 population
print(p_x3)
print(p_x4)


# In[46]:


#test the p value with significance
if p_x3 and p_x4<0.05:
    print("they are not from normal distributions")
else:
    print("they are from normal distributions")


# In[66]:


#mann whitney u test for variables
from scipy import stats
st,p2=stats.mannwhitneyu(x3,x4,alternative='greater')
print(p2)


# In[67]:


#considering 0.05 level of significance
if p2<0.05:
    print("reject null hypothesis")
    print("MIT is more effective than DIT")
elif p2>0.05:
    print("accept null hypothesis")
    print("DIT is more effective than MIT")
else:
    print("not applicable")


# # SCF_heart

# In[49]:


#heart of scf for MIT
x5=df["scf_Heart(%)"]
x5=x5.dropna()
print(x5)


# In[73]:


#heart of scf for DIT
x6=df2["scf_Heart(%)"]
x6=x6.dropna()
print(x6)


# In[74]:


#mean values
import statistics as stat
m5=stat.mean(x5)
print(m5)
m6=stat.mean(x6)
print(m6)


# In[51]:


#shapiro test to check for normality of populations
from scipy import stats
st1,p_x5=stats.shapiro(x5) #shapiro test for x5 population
st2,p_x6=stats.shapiro(x6)#shapiro test for x6 population
print(p_x5)
print(p_x6)


# In[52]:


#test the p value with significance
if p_x5 and p_x6<0.05:
    print("they are not from normal distributions")
else:
    print("they are from normal distributions")


# In[64]:


#mann whitney u test for variables
from scipy import stats
st,p3=stats.mannwhitneyu(x5,x6,alternative='greater')
print(p3)


# In[65]:


#considering 0.05 level of significance
if p3<0.05:
    print("reject null hypothesis")
    print("MIT is more effective than DIT")
elif p3>0.05:
    print("accept null hypothesis")
    print("DIT is more effective than MIT")
else:
    print("not applicable")


# # SCF_LEFTLUNG

# In[55]:


#left lung scf for MIT
x7=df["scf_Lung(%)"]
x7=x7.dropna()
print(x7)


# In[75]:


#left lung scf for DIT
x8=df2["scf_Lung(%)"]
x8=x8.dropna()
print(x8)


# In[76]:


#mean values
import statistics as stat
m7=stat.mean(x7)
print(m7)
m8=stat.mean(x8)
print(m8)


# In[59]:


#shapiro test for normality of populations
from scipy import stats
st1,p_x7=stats.shapiro(x7) #shapiro test for x7 population
st2,p_x8=stats.shapiro(x8)#shapiro test for x8 population
print(p_x7)
print(p_x8)


# In[61]:


#test the p value with significance
if p_x7 and p_x8<0.05:
    print("they are not from normal distributions")
else:
    print("they are from normal distributions")


# In[62]:


#mannn whitney u test for populations
from scipy import stats
st,p4=stats.mannwhitneyu(x7,x8,alternative='greater')
print(p4)


# In[63]:


#considering 0.05 level of significance
if p4<0.05:
    print("reject null hypothesis")
    print("MIT is more effective than DIT")
elif p4>0.05:
    print("accept null hypothesis")
    print("DIT is more effective than MIT")
else:
    print("not applicable")


# Therefore we can conclude that
# 1. For breast: DIT is more effective
# 2. For scf: MIT is more effect

# In[ ]:




