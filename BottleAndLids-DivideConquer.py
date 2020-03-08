#!/usr/bin/env python
# coding: utf-8

# In[43]:


import random

def main():
   
    B = random.sample(range(0, 10), 10)
    C = random.sample(range(0, 10), 10)

    
    bottlesort(B, C, 0, 9)
    
    print(B)
    print(C)


def bottlesort(B, C, lo, hi):
    if lo < hi:
        q = partition(B, lo, hi, C[hi])
        partition(C, lo, hi, B[q])
        bottlesort(B, C, lo, q - 1)
        bottlesort(B, C, q + 1, hi)
    
def partition(A, lo, hi, pivot):
    i = lo
    for j in range(lo, hi):
        if A[j] == pivot:
            temp1 = A[j]
            A[j] = A[hi]
            A[hi] = temp1
            #j = j - 1
        
        if A[j] < pivot:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i = i + 1
       
    temp2 = A[i]
    A[i] = A[hi]
    A[hi] = temp2
    
    return i


# In[44]:


main()


# In[ ]:




