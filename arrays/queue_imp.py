from queue import Queue
q1=Queue()
num=int(input("Enter the size of the queue: "))
for i in range(num):
    x=int(input("Enter the value: "))
    q1.put(x)
# for i in range(q1.qsize()):
#     a=q1.get()
#     if a%3==0 and a%5!=0:
#         print(a)
print(list(q1.queue))

q1.get()
print(list(q1.queue))
