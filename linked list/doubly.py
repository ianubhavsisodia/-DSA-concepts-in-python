# node structure
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyList:
    def __init__(self):
        self.start = None
        self.last = None
    # func to traverse doubly linked list
    def traverse(self):
        temp=self.start
        if temp==None:
            print("List is empty")
        else:
            while temp!=None:
                print(temp.data, end=" ")
                temp=temp.next
    #func to traverse in backward directon
    def backward(self):
        temp=self.start
        while temp.next!=None:
            temp=temp.next
        while temp!=None:
            print(temp.data, end=" ")
            temp=temp.prev
    
    # func to append multiple value
  
        
    # func to insert a new node at the start
    def insertbeg(self, val):
        newnode=Node(val)
        if self.start==None: # if list is empty
            self.start=newnode
        else:
            self.start.prev=newnode
            newnode.next=self.start
            self.start=newnode

    # func to insert a new node at the end 
    def insertatend(self,val):
        newnode=Node(val)
        if self.start==None:
            self.start=newnode
        else:
            temp=self.start
            while temp.next: #or while temp.next!=None:
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp
    # func to insert a new node at a specified position 
    def insertatpos(self,pos,val):
        newnode=Node(val)  
        if pos<1:
            print("\n invalid position ")
        elif pos==1:
            newnode.next=self.start
            self.start.prev=newnode
            self.start=newnode
        else:
            temp=self.start
            for i in range(1,pos-1): #loop to find the node previous to the node to be inserted at the given postion
                if temp!=None:
                    temp=temp.next
            if temp!=None:
                newnode.next=temp.next
                newnode.prev=temp
                temp.next=newnode
                if newnode.next!=None:
                    newnode.next.prev=newnode
            else:
                print("\n node previous to the newnode is null")
    # func to delete the first node
    def del_front(self):
        if self.start==None:
            print("List is empty")
        elif self.start!=None and self.start.next==None:
            self.start=None
        else:
            temp=self.start
            self.start=self.start.next
            temp=None
            #if new start node is not null,then make prev of it as null
            #since prev of start of doubly linked list is null 
            if self.start!=None:
                self.start.prev=None
    #func to delete the last node
    def del_end(self):
        if self.start==None:
            print("List is empty")
        elif self.start!=None and self.start.next==None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next!=None:
                temp=temp.next
            last=temp.next
            temp.next=None
            last=None
    #func to delete a node at a given position
    def del_pos(self,pos):
        if pos<1:
            print("\n invalid position ")
        elif pos==1 and self.start!=None:
            nodetodelete=self.start
            self.start=self.start.next
            nodetodelete=None
            if self.start==None:
                self.start.prev=None
        else:
            temp=self.start
            #traverse to the previous node of the node to be deleted
            for i in range(1,pos-1): 
                if temp!=None:
                    temp=temp.next
            if temp!=None and temp.next!=None:
                nodetodelete=temp.next
                temp.next=temp.next.next
                if temp.next.next!=None:
                    temp.next.next.prev=temp
                nodetodelete=None
            else:
                print("\nThe node is already null")

    # func to delete all nodes
    def delall(self):
        while self.start!=None:
            temp=self.start
            temp=None
            self.start=self.start.next
            
        print("All node are deleted successfully.")
      
    #func to count nodes
    def count(self):
        temp=self.start
        i=0
        while temp!=None:
            i+=1
            temp=temp.next
        print("Total Nodes: {}".format(i,))
    
    #func to count nodes in the backward direction
    def countback(self):
        temp=self.start
        i=0
        while temp.next!=None:
            temp=temp.next
        while temp!=None:
            i+=1
            temp=temp.prev
        print("Total Nodes: {}".format(i,))       
    # func to search an element 
    def search(self, val):
        temp=self.start
        found=1
        if temp!=None:
            while temp!=None:
                if temp.data==val:
                    print(val,"is found at index = {}".format(found,))
                    break
                temp=temp.next
                found+=1
            else:
                print("Not found")
        else:
            print("List is empty")

    # funct to reverse the list 
    def reverse(self):
        if self.start!=None:
            prevnode=self.start
            temp=self.start
            curr=self.start.next

            prevnode.next=None
            prevnode.prev=None
        while curr!=None:
            temp=curr.next
            curr.next=prevnode
            prevnode.prev=curr
            prevnode=curr
            curr=temp

        self.start=prevnode        
       
    # func to delete the palindrome number from the list
    #       



        

             

mylist=DoublyList()
e1=Node(5)
mylist.start=e1
e2=Node(54)         
e1.next=e2
e2.prev=e1
e3=Node(23)
e2.next=e3
e3.prev=e2

mylist.insertbeg(37)
mylist.insertbeg(76)
mylist.insertatend(65)
mylist.insertatend(238)
mylist.insertatpos(5,35)
mylist.insertatpos(5,87)
mylist.traverse()

mylist.reverse()

mylist.traverse()

