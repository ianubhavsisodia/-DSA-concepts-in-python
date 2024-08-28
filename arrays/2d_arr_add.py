import numpy as np
a=np.zeros((3,3))
## to declare all the elements manually
# a[0][0] = 1
# print(a)

for i in range(3):
    for j in range(3):
        values=float(input("Enter the value a[{}][{}]: ".format(i,j)))
        a[i][j]=values
print("\n Matrix-A \n")
for i in range(3):
    for j in range(3):
        print("{}".format(a[i][j],), end=" ")
    print("\n")

b=np.zeros((3,3))
for x in range(3):
    for y in range(3):
        values=float(input("Enter the value b[{}][{}]: ".format(x,y)))
        b[x][y]=values
print("\n Matrix-B \n")
for x in range(3):
    for y in range(3):
        print("{}".format(b[x][y],), end=" ")
    print("\n")

# declaring the resultant matrix
c=np.zeros((3,3))

for m in range(3):
    for n in range(3):
        c[m][n]=a[m][n]+b[m][n]
print("\n Resultant Matrix-C \n")    
for m in range(3):
    for n in range(3):
        print("{}".format(c[m][n],), end=" ")
    print("\n")
