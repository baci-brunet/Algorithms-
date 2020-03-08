#!/usr/bin/env python
# coding: utf-8

# In[28]:


import random


def findIndex(arr):
    
    n = len(arr)
    
    indexArr = []
    for i in range(n+1):
        indexArr.append(0)
        
    for h in range(n):
        if arr[h] >= n: 
            indexArr[n] += 1
        else: 
            indexArr[arr[h]] += 1

    s = 0
    h = n
    while h > 0:
        s += indexArr[h]
        if s >= h:
            return h
        h = h - 1
    return 0

            


# In[29]:


findIndex([6, 5, 3, 1, 0])


# In[ ]:




