#!/usr/bin/env python
# coding: utf-8

# ##### Materials: 
# - download @ https://we.tl/t-XgmO9S5Nm8
# - download @ https://we.tl/t-cI6EvINvMT

# ##### Bonus: https://we.tl/t-1D0pYbkOFZ

# # Introduction

# In[80]:


import pandas as pd
import numpy as np
import os 
import glob


# In[61]:


os.getcwd()


# In[62]:


#os.get() + '\\' + '\\download\\iris.data'     is not recommended


# In[63]:


os.path.join(os.getcwd(),'\\downloads\\iris.data') # concatenate the current 
#directory with the iris.data that is in download


# In[64]:


def check_file(filename):
    '''this function chekcs whether the file exists in the current directory'''
    if os.path.join(os.getcwd(),filename):
        return True
    else:
        return False
# we are doing this because we are working with different data set and
# to make the function is usuable everyt time reading a dtatset 


# In[73]:


check_file('\\downloads\\iris.data')


# In[69]:


def read_dataset(path):
    ''' the function read the data set from the pathe abd return a data frame '''
    if check_file(path) == True:
        df = pd.read_csv(path, header = None)
    else:
        df = None
    return df


# In[70]:


my_path = '\\downloads\\iris.data'


# In[78]:


df_iris = read_dataset('C:\\Users\\Lenovo\\downloads\\iris.data')
df_iris


# In[82]:


def list_files_cur():
    '''
    This function returns the list of the files in the current directory
    '''
    current_directory = os.getcwd()
    result = os.listdir(current_directory)
    return result


# In[83]:


list_files_cur()


# In[84]:


def list_files_with_extension_cur(extension):
    '''
    This function returns the list of the files with a given extension in the current directory
    '''
    current_directory = os.getcwd()
    all_files = list_files_cur() # list all the files in the current directry
    result = [file for file in all_files if file.endswith(extension)] # select only the files finishing with the extension
    return result


# In[86]:


list_files_with_extension_cur('ipynb')


# In[ ]:





# In[ ]:


Today's Lab goals are to get the basic understanding of:
- functions
- pandas
- modules
- data preparation
- train a model ( sklearn)
- evaluate the performance 


# # Part 1 : GitHub 101

# Git clone/push/pull ?
# - https://www.youtube.com/watch?v=yXT1ElMEkW8

# In[ ]:


git clone


# In[ ]:


git status


# In[ ]:


git add .


# In[ ]:


git commit -m


# In[ ]:


git push


# # Part 2 : Datasets

# Many repositories exist:
# - Kaggle (online competitions + prizes)
# - UCI dataset

# In[ ]:


# What can you say about the datasets ?
# what type of data is it, etc.


# In[ ]:





# In[ ]:





# # Part 3 : Data exploration
# - statistics
# - hypothesis
# - plots (matplotlib, seaborn or better : plotly!)
# - outliers

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Part 4 : Data preparation
# - data encoding
# - data standardisation
# - missing values
#     - Mean/median/MICE
#     

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Part 5: Scikit-Learn
# - Train/Validation/Test
# - Algorithm picked (RF, XGBoost...)
# - train algorithm
# - Performance

# https://www.datacamp.com/community/tutorials/random-forests-classifier-python

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




