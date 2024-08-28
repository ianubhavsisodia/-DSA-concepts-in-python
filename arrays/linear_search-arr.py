# linear search of array

#array for searching
arr=[23,55,34,65,8,14,21,19,3,6,17,36,54]

n=int(input("Enter the number to search: "))
#linear search algorithm

for i in range(len(arr)):  ##search loop
    if arr[i]== n:
        print ("Element found at index",i)
        break
if i==12:
    print("No such value exists int the array!")
            
    

#### code to declare array in python    
# from array import *  
# ar=array("i", [1,2,3,4])
# for i in ar:
#     print(i)

#### using numpy 
# import numpy as np
# arr= np.array(10, dtype=int)
# print(arr) 






