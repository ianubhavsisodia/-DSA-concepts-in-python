arr=[]
for i in range(10):
    value=int(input("Enter the value: "))
    arr.append(value)

n=int(input("Enter the value to search for occurance: "))
occ=0 #variable to count the occurances
for i in range(len(arr)): #loop to find the search value
    if n==arr[i]:
        print("{} is present at index {}".format(n,i))
        occ+=1 #if element is present update the occurance
if occ==0:
    print("{} not found".format(n))
else:
    print("Number of occurences: {}".format(occ,))