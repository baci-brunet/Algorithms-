#!/usr/bin/env python
# coding: utf-8

# In[66]:


'''Modified from the following code built from a solution on Quiz 5 that returns a subset in S with a sum == k

def findSum(S, k):
    n = len(S)
    dp = [[False for k in range(k + 1)] for t in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = []

    for i in range(n + 1):
        for j in range(k + 1):
            #LEAVE IT 
            if j < S[i - 1]: #index your looking at is less the ith element in the array
                if dp[i - 1][j] != False: 
                    dp[i][j] = dp[i - 1][j]
            #TAKE IT CONDITION
            else:
                y = False
                if dp[i - 1][j - S[i - 1]] != False:
                    y = dp[i - 1][j - S[i - 1]]
                if y != False and sum(y) + S[i - 1] == j:
                    dp[i][j] = y + [S[i - 1]]
                    
    return dp[n][k]'''

'''Builds the optimal solution using a bottom up implemetation, and solves a 3D array of size nkt. The asymptotic runtime
of this algorithm follows from this; we are filling a table with at most ntk elements and always producing a solution that   
falls in [n][t][k]th cell of our array. The solution to any given cell/problem relies on two subproblems, 
if sum(dp[i - 1][j - S[i - 1]][x - 1]) + S[i - 1] == j and the list is the proper cardinality, we take it. Otherwise, 
we leave it and select the previous element (dp[i - 1][j][x]).'''

def findSum(S, t, k):
    n = len(S)
    
    #Initialize the k (cardinality) dimension to False
    dp = [[[False for k in range(k + 1)] for t in range(t + 1)] for n in range(n + 1)]
    
    #Base Case: 
    for i in range(n + 1):
        dp[i][0][0] = [] #setting an empty set to store the subsets of S
        
    #loops through the k elements which make up a proper subset to be evaluated for sum
    #This loop will only fill the table with sets until they reach cardinality k (k+1 for our 0 base case in table)
    for x in range(k + 1):
        #loops from the first element to the last in S
        for i in range(n + 1): 
            #j represenets any sum value, 0 <= j <= t
            #loops while the next element to be added is not greater than our target sum 
            for j in range(t + 1):
                
                y = False
                if dp[i - 1][j][x] != False:
                    y = dp[i - 1][j][x]
                
                #Leave it condition: if the target sum is less than the value of the element to be added
                #(grab previous element so long as its value is not false)
                if j < S[i - 1]:
                    if y != False:
                        dp[i][j][x] = y
                        
                #Entering a possible "Take it" scenario
                if j >= S[i - 1]:
                    #Must initialize here (screws with the incrementing of the for loops if initialized outside)
                    z = False
                    if dp[i - 1][j - S[i - 1]][x - 1] != False:
                        z = dp[i - 1][j - S[i - 1]][x - 1]
                    
                    #Take it condition: we take this element if adding it yeilds the target sum for this subproblem
                    if z != False and sum(z) + S[i - 1] == j:
                        dp[i][j][x] = z + [S[i - 1]]
                    
                    #Leave it
                    elif y != False:
                        dp[i][j][x] = y
                        
    return dp[n][t][k]
                            
# print(problem_5([2,1,5,7], 6, 2))

def main():
    #S = [9, 7, 6, 2]
    
    S = [1, 2, 3, 4, 5]
    print(f" Subset: {findSubsetSum(S, 6, 3)} ")

if __name__ == '__main__':
    main()


# In[ ]:




