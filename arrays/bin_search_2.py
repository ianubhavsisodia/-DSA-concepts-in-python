a=int(input("Enter the size of the array: "))
print("\n Enter the values in descending order\n")
arr=[]
for i in range(a):
    value=int(input("Enter the value: "))
    arr.append(value)
n=int(input("Enter the value to search: "))

i=0
j=a-1
#initialising the extreme left and right indexes
k=(i+j)//2
#initialising the middle element index
while i<=j:
    if n<arr[k]:
        i=k+1
    elif n>arr[k]:
        j=k-1
    else:
        print("{} is found at position {}".format(n, k))
        break
    k=(i+j)//2 #updating the middle element index before looping the search further


if i>j:
    #not found
    print("{} not found".format(n))