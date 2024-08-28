import numpy as np

a=np.zeros((3,3))

for i in range(3):
    for j in range(3):
        value=float(input("Enter the value a[{}][{}]: ".format(i,j)))
        a[i][j]=value
print("\n MATRIX-A\n")
for i in range(3):
    for j in range(3):
        print("{}".format(a[i][j]), end=" ")
    print("\n")


b=np.zeros((3,3))

for i in range(3):
    for j in range(3):
        value=float(input("Enter the value b[{}][{}]: ".format(i,j)))
        b[i][j]=value
print("\n MATRIX-B\n")
for i in range(3):
    for j in range(3):
        print("{}".format(b[i][j]), end=" ")
    print("\n")

# declaring a new matrix resultant of the two matrix multiplication
c= np.zeros((3,3))
sum=0
for i in range(3):#outer most loop for traversing rows of first matrix
    for j in range(3): # middle loop for travresing columns of second matrix
        for k in range(3):#inner most loop for traversing columns of 1st and rows of second matrix
            
            sum=sum + a[i][k]*b[k][j]
            #end of inner most loop
        c[i][j]=sum
        sum=0 # re-initialisation
        #end of middle loop
    #end of outer loop

print("\n RESULTANT MATRIX-C\n")
for i in range(3):
    for j in range(3):
        print("{}".format(c[i][j]), end=" ")
    print("\n")


