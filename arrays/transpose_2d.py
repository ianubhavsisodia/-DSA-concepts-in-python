import numpy as np

def transpose(a = np.zeros((3,3))):
    b=np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            b[i][j]=a[j][i]
    print("\n Transpose Matrix\n")
    for i in range(3):
        for j in range(3):
            print("{}".format(b[i][j]),"\t",end=" ")
        print("\n") 
    
c=np.zeros((3,3))
for i in range(3):
    for j in range(3):
        c[i][j]=int(input("Enter the value c[{}][{}]: ".format(i,j)))
print("\n Matrix\n")
for i in range(3):
        for j in range(3):
            print("{}".format(c[i][j]),"\t",end=" ")
        print("\n")    

transpose(c)

# l1=[int]
# * 5 # list of integers