mx=int(input("Enter the size of array: "))
arr=[]
for i in range(mx):
    value=int(input("Enter the value: "))
    arr.append(value)

for i in range(0,mx-1):
    for j in range (i+1 , mx ):
        if arr[i]<arr[j]:  # for decsending order
            temp =  arr[i]
            arr[i]=arr[j]
            arr[j]=temp

print(arr)