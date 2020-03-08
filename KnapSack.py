#!/usr/bin/env python
# coding: utf-8

# In[72]:


def proShake(C, cal, p): 
    n = len(p)
    S = [[0 for x in range(C+1)] for x in range(n+1)] 
    for i in range(n+1): 
        for c in range(C+1): 
            if i==0 or c==0: 
                S[i][c] = 0
            elif cal[i-1] <= c: 
                S[i][c] = max(p[i-1] + S[i][c-cal[i-1]],  S[i-1][c]) 
            else: 
                S[i][c] = S[i-1][c] 

    return S[n][C] 

def main():   
    p = [5, 6, 2] 
    cal = [3, 5, 4] 
    C = 10
    print(proShake(C, cal, p)) 


# In[73]:


main()


# In[ ]:





# In[ ]:





# In[ ]:




