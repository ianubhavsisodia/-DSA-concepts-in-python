from collections import deque
num1=int(input("Enter the size of stack1: "))
stack1=deque()
for i in range (num1):
    a=int(input("Enter the value: "))
    stack1.append(a)
print("Stack 1: ",list(stack1))

num2=int(input("Enter the size of stack2: "))
stack2=deque()
for i in range (num2):
    b=int(input("Enter the value: "))
    stack2.append(b)
print("Stack 2: ",list(stack2))

stack3=deque()
for i in range(len(stack1)):
    x=stack1.pop()
    stack3.append(x)
for j in range(len(stack2)):
    y=stack2.pop()
    stack3.append(y)

print("Stack 3: ",list(stack3))