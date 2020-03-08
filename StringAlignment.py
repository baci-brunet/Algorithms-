#!/usr/bin/env python
# coding: utf-8

# In[7]:


def alignString(x, y, c_insert, c_delete, c_sub):
    
    nx = len(x) + 1
    ny = len(y) + 1
    
    C = [[0 for i in range(ny)] for j in range(nx)]
    
    for i in range(nx):
        for j in range(ny):
        
            #If first string is empty
            if i == 0 and j >= 1:
                C[i][j] = C[i][j-1] + c_insert
            #If second string is empty
            elif j == 0 and i >= 1:
                C[i][j] = C[i-1][j] + c_delete
    
    #After 0 case is handled for x and y
    for m in range(1, nx):
        for n in range(1, ny):
            
            #use x, y of [i-1] because our cost table has one more row and column than our original strings
            if x[m-1] == y[n-1]: 
                sub = 0
            else:
                sub = c_sub
            
            #Calculate min value with proper substitution cost
            C[m][n] = min(C[m-1][n] + c_delete, C[m][n-1] + c_insert, C[m-1][n-1] + sub)
            
    return C

'''This function creates the cost table for the alignment of my two strings.
   To begin with I initialize my array to the proper size with value 0 in every cell. 
   I then cover my base case (0th row and column of my cost array), which represents the insert and delete operations
   I would have to use to create my target string. Then I loop through my cost array (starting at the 1st row and column)
   and check what operations I would have to use to transform my source string into the target. If the letters we are on 
   are the same we perform a no-op (substitution with cost 0) and if they are different we choose the operation with the minimum
   cost of the three (insert, sub, delete).'''
    


def extractAlignment(C, x, y, c_insert, c_delete, c_sub):
    i = len(x)
    j = len(y)
    
    ops = []
    
    #Backtracking without breaking ties
    while i > 0 and j > 0:
       

        '''If all the conditions are the same then we can add the three to a list of "ties".
           Then we take random.choice from list and use that in our ops array. This will produce 
           different optimal solutions depending on which subproblem was chosen.'''

        if C[i][j] == C[i][j-1] + c_insert: #insert
            ops.insert(0, 'c_insert')
            j = j-1

        if C[i][j] == C[i-1][j] + c_delete: #delete
            ops.insert(0, 'c_delete') 
            i = i-1

        if C[i][j] == C[i-1][j-1] + c_sub: #cost sub
            ops.insert(0, 'c_sub')
            i = i-1
            j = j-1

        elif C[i][j] == C[i-1][j-1]: #no cost sub
            ops.insert(0, 'no-op')
            i = i-1
            j = j-1
    
    while i != 0:
        ops.insert(0, 'c_delete')
        i = i-1
        
    while j != 0:
        ops.insert(0, 'c_insert')
        j = j-1
        
    return ops

'''This function creates the list of operations that were used in aligning the two strings. I backtrack, starting with the bottom rightmost element in the cost 
   array (cell[len(x)][len(y)]), and check which subproblem (i.e. S[i-1][j], S[i][j-1], S[i-1][j-1]) was used to find the cell I am currently on. I then decrement 
   i and j depending on which subproblem is used. I add the operation to a list consisting of all the edits made to align the strings. I must also account for the 
   fact that i can reach 0 before j does and vice versa. In this case, we add the respective base case operation (insert or delete) to our list until we arrive at 
   cell[0][0]'''

'''I should have had my function check the case in which there was a tie (several options for the operation we could have used) 
   and "broke it", by randomly selecting one of the operations. I could have done this by creating a sub list for each cell consisting of every valid operation to get there, 
   and then taking a random.choice from it for the ops array. Instead it chooses based on order of the if statements.'''
                

def commonSubstring(x, L, a):
    
    
    substrings = []
    substring = ""
    
    i = 0
    
    #cast x to an array. Then where you find an "insert" add a "_" so the lengths of a and x are the same
    
    for op in a:
        if op == 'no-op':
            substring += x[i]     
    
        else:
            if len(substring) >= L:
                substrings.append(substring)
            substring = ""   
            
        if op != 'c_insert':
            i = i+1
            
       
    if (substring != "" and len(substring) >= L):
        substrings.append(substring)
            
    return substrings
    
    '''This function checks for common substrings of at least length L between the two strings. I start by looping
       through the operations array returned in my extractAlignment function. This will tell me when we encountered 
       two letters in the strings that were the same, denoted by a 'no-op'. Once we hit our first no-op, we append 
       the corresponding letter to a substring and then hit our second if statement and i increments. This continues 
       until we reach an operation that is not a no-op. Note that when we hit an insert operation we do not increment i 
       because we are staying in the same position in the string. When we hit a delete operation after a series of 
       no-ops, we check that our substring is >= L, and if so, append it to our list of common substrings and clear the 
       substring itself. After the loop terminates we check a if our substring is empty, and if it is both not empty 
       and >= L, we append the substring to our list '''
                
        
    #ASYPTOTIC ANALYSIS
        
    '''My alignStrings function has a O(x * y). In the worst case, we will see x * y cells filled/operations performed.
       In my extractAlignment function, the time compexity we see is O(x + y). In the worst case our 
       optimal path traces back across the last row until j hits zero, but i has not moved, then see that we get y number
       of base case operations until i hits 0 and therefore see x + y operations done. In my commonSubstring function we see
       O(x + y) run time because in the worst case our operations array will delete the entire string x and insert the entire string y.'''
    
def main():
    
    #########################################
    
    #FOR THE TWO STRINGS
    
    #########################################
    
    x = 'EXPONENTIAL'
    y = 'POLYNOMIAL'
    
    c_insert = 2
    c_delete = 1
    c_sub = 2
    L = 2
    
    C = alignString(x, y, c_insert, c_delete, c_sub)
    print("My cost array is \n", C)
    ops = extractAlignment(C, x, y, c_insert, c_delete, c_sub) 
    print("The common substrings between these two words of length >= 2\n", commonSubstring(x, L, ops))
    
    #########################################
    
    #FOR THE TWO SONGS
    
    #########################################
    
    z = "I hear the train a-comin, it's rolling 'round the bend  And I ain't been kissed lord since I don't know when  The boys in Crescent City don't seem to know I'm here  That lonesome whistle seems to tell me, Sue, disappear    When I was just a baby my mama told me, Sue  When you're grown up I want that you should go and see and do  But I'm stuck in Crescent City just watching life mosey by  When I hear that whistle blowin', I hang my head and cry    I see the rich folks eatin' in that fancy dining car  They're probably having pheasant breast and eastern caviar  Now I ain't crying envy and I ain't crying me  It's just that they get to see things that I've never seen    If I owned that lonesome whistle, if that railroad train was mine  I bet I'd find a man a little farther down the line  Far from Crescent City is where I'd like to stay  And I'd let that lonesome whistle blow my blues away" 
    l = "I hear the train a comin' it's rollin' round the bend  And I ain't seen the sunshine since I don't know when  I'm stuck in Folsom Prison and time keeps dragging on  But that train keeps a rollin' on down to San Antone.    When I was just a baby my mama told me son  Always be a good boy don't ever play with guns  But I shot a man in Reno just to watch him die  When I hear that whistle blowin' I hang my head and I cry.    I bet there's rich folks eatin' in a fancy dining car  They're probably drinkin' coffee and smokin' big cigars  But I know I had it comin' I know I can't be free  But them people keep a movin' that's what tortures me.    Well if they freed me from this prison if that railroad train was mine  I bet I'd move it on a little farther down the line  Far from Folsom Prison that's where I want to stay  And I'd let that lonesome whistle blow my blues away" 
    
    S = alignString(z, l, 1, 1, 1)
    
    ops2 = extractAlignment(S, z, l, 1, 1, 1)
    
    cs = commonSubstring(z, 10, ops2)
    
    #count words in list of substring
    count = 0
    for string in cs:
        count += len(string)
    
    similarity = (count / len(z))*100
    
    print("These two songs are approximately", similarity, "%", "similar")
    
    return
    

    
  
    
    

    

