# reads size of an array from the user
# reads array elements from the user and print the highest value

## code using MAX function
'''n=int(input("Enter the size of array: "))
arr=[]
for i in range(n):
    num=float(input("Enter the elements: "))
    arr.append(num)

print('The maximum element is',max(arr))'''
    

## 
n=int(input("Enter the size of array: "))
arr=[]
for i in range(n):
    num=float(input("Enter the elements: "))
    arr.append(num)

# initialize biggest as first element 
biggest = arr[0]
for j in range(1,len(arr)):
    # if current number is greater than previous one, then update it
    if arr[j]>biggest:
        biggest = arr[j]
    
print("The biggest value is {}".format(biggest,))
