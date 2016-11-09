
# coding: utf-8

# ### Lets start by importing the necassary packages and creating a connection to our database.

# In[2]:

import sqlite3


# In[3]:

conn = sqlite3.connect("fire.sqlite")


# In[4]:

c = conn.cursor()


# No Normalization needed because there has been no need. (Database is not big so join time will outweigh pros of reducing space.)
# 
# ### Next we grab our table names.

# In[7]:

c.execute("SELECT name FROM sqlite_master WHERE type = 'table'")


# This Points the cursor at what we want (name from the table sqlite_master)

# In[ ]:

print c.fetchall()


# This Prints what is at the Cursor
# 
# ### Next we look for the column names in our table.

# In[9]:

c.execute("PRAGMA table_info(fire)")


# In[10]:

print c.fetchall()


# Note that this command gives lots of information, all we really need for now is Column Name.
# The format goes (COLUMN NUMBER,u'COLUMN NAME',u'DATA TYPE',...)
# 
# ### Next let's find only the fires caused by lightning
# CAUSE is the 8th column (count starts at 0).
# Note that the CAUSE code for lightning is 1, this is outside information not included in the table.

# In[11]:

c.execute("SELECT * FROM fire WHERE CAUSE == 1")


# In[12]:

print c.fetchall()


# This output is hard to read but just take a cursory glance and make sure the 8th spot is 1.
# 
# ### Now that we have this selection lets make a new table based on it.
# To create a new table from a subset of this existing table we will use CREATE TABLE AS, this syntax for which is:
# CREATE TABLE new_table AS SELECT expressions FROM existing_tables WHERE conditions

# In[13]:

c.execute("CREATE TABLE lightfire AS SELECT * FROM fire WHERE CAUSE == 1")


# The Cursor is a temporary operation, you must commit your operation!

# In[15]:

conn.commit()


# Let's make sure our new table is in the database.

# In[16]:

c.execute("SELECT name FROM sqlite_master WHERE type = 'table'")


# In[17]:

print c.fetchall()


# In[18]:

c.execute("SELECT * FROM lightfire")


# In[19]:

print c.fetchall()


# Everything Looks Good!

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



