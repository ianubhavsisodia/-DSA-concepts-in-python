## find the smallest no. from the array
n=int(input("Enter the size of the array: "))
arr=[]
for i in range(n):
    num=float(input("Enter the elements: "))
    arr.append(num)

smallest = arr[0]

for j in range(1,len(arr)):
    if arr[j]<smallest:
        smallest=arr[j]
    
print("\nThe smallest number is {}".format(smallest,))

if (smallest==arr[0]): sec_smallest =arr[1]
else:
    sec_smallest=arr[0]

for x in range(1,len(arr)):
    if arr[x]<sec_smallest and arr[x]!=smallest:
        sec_smallest=arr[x]
    
   
print("\nThe second smallest number is {}".format(sec_smallest,))