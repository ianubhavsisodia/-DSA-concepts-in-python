# reads number from the user into an array
#print their sum and avg.

arr=[]
n=0
sum=0
while n<5:
    num = int(input("Enter a number: "))#get input as integer
    arr.append(num)
    sum+=arr[n]
    n+=1

print("\n",arr,"\n")
print("Sum = {} \nAverage = {}".format(sum, sum/5))




