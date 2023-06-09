#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv("movies.csv")
df.head()


# In[3]:


df.info()


# # Coverting object into int

# In[4]:


df['imbd_votes'] = df['imbd_votes'].str.replace(',', '').astype(int)
df.info()


# # find out movies of each genre which has maximum number of votes.

# In[5]:


df['imbd_votes'].max()


# In[6]:


df1=df.loc[df['imbd_votes']==2711075]
df1[["title","imbd_votes","genre","duration"]]


# # find out which movie has the minimum number of votes and which genre it belongs to and its duration.

# In[7]:


df["imbd_votes"].min()


# In[8]:


df1=df.loc[df['imbd_votes']==31167]
df1[["title","imbd_votes","genre","duration"]]


# # Plot a graph to show the distribution of genre in the top 250 movies

# In[10]:


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='imbd_rating', y='imbd_votes', hue='genre', alpha=0.5, palette='dark')
plt.title('IMDb Ratings vs. Votes for Top 250 Movies by Genre')
plt.xlabel('IMDb Rating')
plt.ylabel('Votes')
plt.legend(title='Genre')
plt.show()


# # find out movies of each genre which has maximum number of votes.

# In[11]:


gp=df.groupby("genre").agg({"imbd_votes":max})
print(gp)


# In[ ]:




