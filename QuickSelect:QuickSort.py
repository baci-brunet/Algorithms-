#!/usr/bin/env python
# coding: utf-8

# In[15]:


import math
import random

def partition(arr, low, high): 
    pivot = arr[high]    
    i = low - 1
    for j in range(low , high): 
        if  arr[j] <= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
        if i >= 6:
            print(arr)
            
    arr[i + 1],arr[high] = arr[high],arr[i + 1] 
    return i + 1 
    
# finds pivot value

def quickselect(A, l, r, split):
    split = 1/4
    k = int((r-l)*split)
    pi = partition(A, l, r)
    
    if pi == r:
        return pi
    
    if k == pi:
        return pi
    elif k > pi:
        return quickselect(A, l, pi - 1, split) #k instead of pi?
    else:
        return quickselect(A, pi + 1, r, split) #k instead of pi?
        
    
def quickSort(arr, lo, hi): 
    split = None
    if lo < hi: 
        pi = quickselect(arr, lo, hi, split)
        pi = pi + lo
        
        print(arr)
        print(arr[lo:pi])
        print(arr[pi + 1: hi])
    
        quickSort(arr, lo, pi - 1) 
        quickSort(arr, pi + 1, hi) 
   
        
def main(n):
    arr = random.sample(range(0, n), n)
    x = len(arr) 
    quickSort(arr, 0, x - 1) 
    print ("Sorted array is:") 
    for i in range(x): 
        print ("%d" %arr[i]), 


# In[16]:


main(2)
main(4)
main(8)
main(16)
main(32)
main(64)
main(128)
main(256)
main(512)
main(1024)
main(2048)
main(4096)


# In[ ]:





# In[ ]:




