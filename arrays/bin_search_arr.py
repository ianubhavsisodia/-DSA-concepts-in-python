a=int(input("Enter the size of the array: "))
arr=[]
print("\n Enter the array values in ascending order\n")
for i in range(a):
    value=int(input("Enter the value: "))
    arr.append(value)

n=int(input("Enter the number to search: "))
#binary search algorithm
i=0
j=a-1
#initializing variables i and j for left and right index of array respectively.
k=((i+j)//2)
#initializing k with middle element of array

while i<=j:
    if n>arr[k]:    #if element is greater than mid then it will be searched in the right half of the array
        i = (k + 1) #incrementing i by one as we are searching from next location onwards
    elif n<arr[k]:  #if element is lesser than mid then it will be searched in the left half of the array
        j=(k-1)     #decrementing j by one as we are searching from previous location onwards
    else:
        print ("Element found at position", k)
        break   
    k=(i+j)//2 #updating the value of middle element 

if i>j:
    print('element not present')