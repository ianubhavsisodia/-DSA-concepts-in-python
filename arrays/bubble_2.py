a= int(input("Enter the size of array: "))
arr = []  # creating an empty list to store elements in it.
for i in range(a):
    value=int(input("Enter the value: "))
    arr.append(value)
flag=0
for i in range(0,a-1):
    for j in range(0,(a-1)-i):
        if arr[j]>arr[j+1]:
            temp=arr[j]   ## swapping two values at index j and (j+1).
            arr[j]=arr[j+1]
            arr[j+1]=temp
            flag+=1 #increment the value by 1 indicating that interchanging took place in the current pass

            
    if flag==0: #no interchanging took place in the pass just concluded, thus indicating that array has turned sorted, no need to go for more passes
        break
    else:
        flag=0 # reinitialising the value with 0

print(arr)