# reads the temperature of a city for the last 10 days into an array
list1=[]
n=0
while n<10:
    temp = int(input("Enter the temperature for day",n+1)) #taking input from user
    list1.append((temp))   #adding elements to the list
    n+=1
n=0
while n<10:
    print("\nTemperature of day {} is {}".format((n+1),list1[n]))
    n+=1
