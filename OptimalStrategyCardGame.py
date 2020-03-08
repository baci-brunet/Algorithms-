#!/usr/bin/env python
# coding: utf-8

# In[24]:


import random 

'''I am doing a bottom-up implentation to fill my dp table. After every iteration of the outer for loop, j resets to spc (the outer loop iterator)
and i resets to 0. After every iteration of the inner loop, j increments and i is set to  This way we fill our table diagonally on every iteration of the outer for loop. 
On the first iteration of our outer for loop we hit one of our base cases (subsets of 1 card) and the diagonal of our dp table is filled with the entire set of cards. 
On the second iteration, we hit our second base case (Subsets of 2 cards) and we fill the next diagonal with the min of the two card values S[i],S[j].
The cells/subproblems we require to produce an optimal solution are dp[i+2][j]), dp[i+1][j-1] and dp[i][j-2].'''

'''There are two choices: 
   Player 1 chooses the ith card with value S[i]: Player 2 either chooses (i+1)th card or jth card. 
   Player 2 intends to choose the card with minimum value, leaving the max of the two cards behind for player 1. 
   Therefore player 1 can collect the value S[i] + max( dp(i+2, j), dp(i+1, j-1) ) 
   

   Player 1 chooses the jth card with value S[j]: Player 2 either chooses ith card or (j-1)th card. 
   Player 2 intends to choose the coin with minimum value, leaving the max of the two cards behind for player 1. 
   Therefore player 1 can collect the value S[j] + max( dp(i+1, j-1), dp(i, j-2) )
   
   Player 1 will then choose between the minimum of these two possible plays and move forward'''

'''Base Cases
     If j == i:
        dp[i][j]  = S[i]   
     If j = i + 1
        dp[i][j] = min(S[i], S[j]) 

     Else:
     dp[i][j] = min(S[i] + min(dp[i+2][j]), dp[i+1][j-1]), S[j] + min(dp[i+1][j-1], dp[i][j-2]))'''

def optimalChoice(S): 
    n = len(S)
     
    dp = [[0 for i in range(n)] for i in range(n)] #dp table of size n by n 
    
    sol = []
    
    #spc represents the spacing value between i and j
    
    #Base Case 1: On the FIRST iteration of the OUTER for loop, spc = 0 and the inner loop begins with j, i set to 0. 
    #j, i are equal and increment together until they reach the end of the row of cards.
    #Base Case 2: On the second iteration of the outer for loop spc = 1 and for every iteration of the inner for loop
    #i and j will be 1 apart. So we take the minimum of the two cards at indices i, j. 
    for spc in range(n):
        #Inner loop resets i to 0 and j to spc. 
        for j in range(spc, n): 
            i = j - spc
            count = 0
            x = 0
            y = 0
            z = 0
            
            if((i + 2) <= j): 
                x = dp[i + 2][j] 
            
            if((i + 1) <= (j - 1)): 
                y = dp[i + 1][j - 1] 
            
            if(i <= (j - 2)): 
                z = dp[i][j - 2] 
                
            #For first base case, only diagonal is filled with all values of S + 0 because x, y, z remain 0 through first iteration of outer loop
            #For the second base case, we fill the table diagonally with the minimum of S[i], S[j] where j = i + 1
            
            
            dp[i][j] = min(S[i] + max(x, y), S[j] + max(y,z))
    
    
    '''Note this is probably not space optimized as I only fill/require an upper triangular matrix to solve. However
    this question did not have a space usage requirement so I simply used a 2D array'''
    
    #Uncomment to print dp array
    
#     for item in dp:
#         print(item)
    
    return dp[0][n - 1] #upper rightmost cell

def main():
    #Uncomment for test case
    #S = [5, 2, 7, 3, 4, 6] 
    S = random.sample(range(0, 100), 100)
    x = optimalChoice(S)
    
    #Subtract x from S to get player 2's sum
    s = sum(S) - x
    
    print(f" player 1 score: {x} \n player 2 score: {s}" )

if __name__ == '__main__':
    main()
    
   

