#!/usr/bin/env python
# coding: utf-8

# In[15]:


import random



def createArray(n):
    arr = []
    for i in range(n):
        arr.append(i + 1)
    random.shuffle(arr)
    return arr
    
def countFlips1(arr):
    size = len(arr)
    flips = 0
    for i in range(size): 
        for j in range(i + 1, size): 
            if (arr[i] > arr[j]):
                flips += 1
    return flips 
    
def mergeSort(arr):
    size = len(arr)
    temp_arr = []
    for i in range(size):
        temp_arr.append(0)
    return countFlips2(arr, temp_arr, 0, size-1)


  
def countFlips2(arr, temp_arr, left, right): 
    flips = 0
    if left < right: 
        mid = (left + right)//2
        
        flips = countFlips2(arr, temp_arr, left, mid) 
        
        flips += countFlips2(arr, temp_arr, mid + 1, right) 
        
        flips += mergeArrays(arr, temp_arr, left, mid, right) 
        
    return flips 
  

def mergeArrays(arr, temp_arr, left, mid, right): 
    l = left     
    m = mid + 1 
    n = left      
    flips = 0
  
    while l <= mid and m <= right:   
        #No inversion 
        if arr[l] <= arr[m]: 
            temp_arr[n] = arr[l] 
            n += 1
            l += 1
        else: 
            # Inversion  
            temp_arr[n] = arr[m] 
            flips += (mid-l + 1) 
            n += 1
            m += 1
  
    while l <= mid: 
        temp_arr[n] = arr[l] 
        n += 1
        l += 1
  
    while m <= right: 
        temp_arr[n] = arr[m] 
        n += 1
        m += 1
  
    # Copy the sorted subarray into Original array 
    for i in range(left, right + 1): 
        arr[i] = temp_arr[i]      
    return flips
 
#Run main with the number you would like to use as the range for 
#our randomly generated array. Then the function will execute countFlips1 and 2 
#on the array [2, ..., 4096] and print all the results
def main(n):
    arr1 = createArray(n)
    
    print("# of flips on random array (simple case):", countFlips1(arr1))   
    print("# of flips on random array (complex case):", mergeSort(arr1))
   
    


# In[17]:


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

