# reads values into the elements of a 2D array and prints then
import numpy as np
scores = np.zeros((3,3)) #here zeros((x,y)) func takes the shape as parameter and returns an array of the given shape, values initialised to zero
# score is an 3x3 matrix with all elements are set to zero

## setting the user defined values to the scores matrix
for i in range(3):
    for j in range(3):
        values=int(input("Enter the value [{}][{}]: ".format(i,j)))
        scores[i][j]=values
        
print("\n Matrix\n")
for i in range(3):
    for j in range(3):
        print(scores[i][j],"\t",end=" ")
    print("\n")    