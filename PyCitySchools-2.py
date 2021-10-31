#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Add the Pandas dependency.
import pandas as pd


# In[7]:


# Files to load
school_data_to_load = "Desktop/schools_complete.csv"
student_data_to_load = "Desktop/students_complete.csv"


# In[8]:


# Add the dependencies.
import pandas as pd
import os


# In[11]:


# Files to load
school_data_to_load = os.path.join("Desktop", "schools_complete.csv")
student_data_to_load = os.path.join("Desktop", "students_complete.csv")


# In[12]:


# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df


# In[13]:


# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()


# In[ ]:




