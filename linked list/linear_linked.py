#Creating a linked list
#Class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Class to create the Linked List
class LinkedList:
    def __init__(self):
        self.start = None
        self.last = None
    
    # func to add elements after creating the linked list
    def append(self,value):
        if self.last==None:
            self.start=Node(value)
            self.last=self.start
        else:
            self.last.next=Node(value)
            self.last=self.last.next

    # func for traversing / printing
    def view(self):
        temp = self.start
        while (temp != None):
            print(temp.data,end=" ")
            temp = temp.next
    # func for inserting a node at the beginning
    def insertbeg(self, value):
        newnode=Node(value)
        if (self.start == None):
            self.start = newnode
            return
        else:
            temp = self.start
            self.start = newnode
            newnode.next = temp
    # func for inserting a node at a given position
    def insertatpos(self,nodeatpos,value):
        if nodeatpos==None:
            print("Mentioned node is invalid")
            return
        newnode=Node(value)
        newnode.next=nodeatpos.next
        nodeatpos.next=newnode
    # func for inserting a node at the end
    def insertend(self,value):
        newnode = Node(value)
        if self.start == None:
            self.start=newnode
            return
        else:
            temp=self.start
            while temp.next:
                temp=temp.next
            temp.next=newnode
    # func for searching the element
    def search(self,value):
        temp=self.start
        index=1
        if temp!=None:
            while temp!=None:
                if temp.data==value:
                    print("Element found at index =",index)
                    break
                temp = temp.next
                index+=1
            else:
                print("Not found")
        else:
            print("empty list")
    # func to reverse the linked list
    def reverse(self):
        prev=None
        curr=self.start
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.start=prev
    # func to remove an element 
    def remove(self,val):
        temp=self.start
        if temp!=None:
            if temp.data==val:
                self.start=temp.next
                temp=None
                return
        while temp!=None:
            if temp.data==val:
                break
            prev=temp
            temp=temp.next
        if temp==None:
            return
        prev.next=temp.next
        temp=None
    # fync to delete negative node from the linked list
    def delnegative(self):
        temp=self.start
        prev=None
        while temp:
            if temp.data<0:
                if temp==self.start:
                    self.start = temp.next
                    temp=self.start
                else:
                    prev.next=temp.next
                    temp=temp.next
            else:
                prev=temp
                temp=temp.next        


l1=LinkedList()
while True:
    print("\n***************MENU***************\n") 
    print("1. Create linked list and add elements \n2. Insertion in Beginning \n3. Insertion at Position \n4. Insertion at End \n5. Print Linked List \n6. Search an element \n7. Reverse the Linked List \n8. Delete an element \n9. Delete negative node \n ")
    user_input=int(input("Enter your choice: "))
    if user_input==1:
        num=int(input("Enter the size of the Linked List: "))
        for i in range(num):
            val=int(input("Enter the value {}: ".format(i+1,)))
            l1.append(val)
    elif user_input==2:
        num1=int(input("Enter the value to add at the beginning: "))
        l1.insertbeg(num1)
    elif user_input==3:
        pos=int(input("Enter the position: "))
        num2=int(input("Enter value to insert at position {}: ".format(pos,)))
        l1.insertatpos(pos,num2)
    elif user_input==4:
        num3=int(input("Enter the value to add at the end: "))
        l1.insertend(num3)
    elif user_input==5:
        print("Linked List:",end=" "),l1.view()
    elif user_input==6:
        val=int(input("Enter the element to search: "))
        l1.search(val)
        
    elif user_input==7:
        l1.reverse()
    elif user_input==8:
        val=int(input("Enter the value to remove: "))
        l1.remove(val)
    elif user_input==9:
        l1.delnegative()
    
    ask=input("\nDo you want to continue? (Y/N) \n").capitalize()
    if ask=="Y":
        continue
    else:
        break

