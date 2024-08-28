a=int(input("Enter the size of array: "))
arr=[]
for i in range(a):
    value=int(input("Enter the value: "))
    arr.append(value)

for i in range(0,a-1): #outer loop for passes  (a-1) beacuse passes are 1 less than the total elements
    for j in range(0,(a-1)-i): # inner loop for comparison (a-1)-i beacuse comparison will be reduced by 1 after each pass
        if (arr[j]>arr[j+1]):
            temp = arr[j] # declaring temp var for swapping the values
            arr[j]=arr[j+1]
            arr[j+1]=temp
            #end of if statement
        #end of inner loop
    #end of outer loop

print("Sorted array is {} ".format(arr))