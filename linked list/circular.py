class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class CircularList:
    def __init__(self):
        self.start=None
        self.last=None
    
    #func to traverse the circular linked list
    def traverse(self):
        print(self.start.data)
        temp=self.start.next
        while temp!=self.start:
            print(temp.data)
            temp=temp.next
       
    #func to insert a node at the beginning 
    def insertbeg(self,val):
        newnode=Node(val)
        #check if list is empty, if yes, then make new node as start
        if self.start==None:
            self.start=newnode
            newnode.next=self.start
        else:
            temp=self.start
            while temp.next!=self.start: #loop to find the address of last node
                temp=temp.next
            newnode.next=self.start
            self.start=newnode #updating value of start
            temp.next=self.start #linking last node to the new node
    
    #func to add a new node at the end
    def insertend(self,val):
        newnode=Node(val)
        if self.start==None:
            self.start=newnode
            newnode.next=self.start
        else:
            temp=self.start
            while temp.next!=self.start:
                temp=temp.next
            temp.next=newnode
            newnode.next=self.start
    
    #func to add a new node a given position
    def insertatpos(self,pos,val):
        newnode=Node(val)
        temp=self.start
        #find no. of elements in the list
        count=0
        if temp!=None:
            count+=1
            temp=temp.next
        while temp!=self.start:
            count+=1
            temp=temp.next 
        
        if pos>count+1 or pos<1:
            print("\nInvalid position")
        elif pos==1:
            if self.start==None:
                self.start=newnode
                newnode.next=self.start
            else:
                while temp.next!=self.start:
                    temp=temp.next
                newnode.next=self.start
                self.start=newnode
                temp.next=self.start
        elif pos==count+1:
            if self.start==None:
                self.start=newnode
                newnode.next=self.start
            else:
                while temp.next!=self.start:
                    temp=temp.next
                temp.next=newnode
                newnode.next=self.start
        else:
            for i in range(1,pos-1):
                temp=temp.next
            newnode.next=temp.next
            temp.next=newnode

    #func to delete the first node
    def delfirst(self):
        if self.start==None:
            print("List is empty")
        elif self.start!=None:
            if self.start.next==self.start:
                self.start=None
            else:
                temp=self.start
                first=self.start
                while temp.next!=self.start:
                    temp=temp.next
                self.start=self.start.next
                temp.next=self.start
                first=None
    # func to delete the last node
    def dellast(self):
        if self.start==None:
            print("List is empty")
        elif self.start!=None:
            if self.start.next==self.start:
                self.start=None
            else:
                temp=self.start
                #loop for traversing to find second last node
                while temp.next.next!=self.start:
                    temp=temp.next
                last=temp.next
                temp.next=self.start
                last=None

    # func to delete a node at a given position
    def deleteatpos(self,pos):
        nodetodelete=self.start
        temp=self.start
        count=0
        #find the number of elements in the list
        if temp!=None:
            count+=1
            temp=temp.next
        while temp!=self.start:
            count+=1
            temp=temp.next
        #check if specified positiion is valid
        if pos>count or pos<1:
            print("\nInvalid position")
        elif pos==1:
            if self.start.next==self.start:
                self.start=None
            else:
                while temp.next!=self.start:
                    temp=temp.next
                self.start=self.start.next
                temp.next=self.start
                nodetodelete=None
        elif pos==count:
            if self.start.next==self.start:
                self.start=None
            else:
                while temp.next.next!=self.start:
                    temp=temp.next
                nodetodelete=temp.next
                temp.next=self.start
                nodetodelete=None
        else:
            for i in range(1,pos-1):
                temp=temp.next
            nodetodelete=temp.next
            temp.next=temp.next.next
            nodetodelete=None           
    #func to delete all the nodes
    def clearList(self):
        if self.start==None:
            print("List is empty")
        elif self.start!=None:
        # if current node is not equal to head, delete the
        # current node and move current to next node using temp,
        # repeat the process till the current reaches the head
            cur=self.start.next
            while cur!=self.start:
                temp=cur.next
                cur=None
                cur=temp
            self.start=None
        print("All nodes are deleted successfully")

    #code challenge internshala 1
    def printrange(self,r1=120,r2=255):
        if self.start==None:
            print("List is empty")
        elif r1<=self.start.data<=r2:
            print(self.start.data)
        
        temp=self.start.next
        if self.start!=None:
            while temp!=self.start:
                if r1<=temp.data<=r2:
                    print(temp.data)
                temp=temp.next
    #code challenge 2
    def remove_first_zero(self):
        
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            first=self.start
            while self.start.data==0:
                while temp.next!=self.start:
                    temp=temp.next
                self.start=self.start.next
                temp.next=self.start
                first=None
            
    
mylist=CircularList()
            
# mylist.start=Node(2)
# e2=Node(23)
# e3=Node(45)
# e4=Node(67)
# mylist.start.next=e2
# e2.next=e3
# e3.next=e4
# e4.next=mylist.start
mylist.insertbeg(3)
mylist.insertbeg(0)
mylist.insertbeg(0)
mylist.insertbeg(0)
mylist.insertend(213)
mylist.insertend(34)
mylist.insertend(250)
# mylist.deleteatpos(4)

# mylist.insertatpos(1,12)
# mylist.traverse()
# mylist.printrange()
mylist.remove_first_zero()
mylist.traverse()