a=int(input("Enter the size of the array: "))
arr=[]
for i in range(a):
    value=int(input("Enter the value: "))
    arr.append(value)

for i in range(0,a-1):  #outer loop for passes  (a-1) beacuse passes are 1 less than the total elements
    for j in range(i+1,a): #inner loop for comparison 
        if arr[i]>arr[j]:
            temp = arr[i]
            arr[i]=arr[j]
            arr[j]=temp

print("Sorted array is {} ".format(arr,))