import numpy as np
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    def insert(self,data):
        # compare the new value with the parent node
        if self.data: # parent node
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def preorder(self,root):
        # stack=[]
        # stack.append(root)
        # if root==None:
        #     return
        # while len(stack)>0:
        #     temp=stack.pop()
        #     print(temp.data)
        #     if temp.right!=None:
        #         stack.append(temp.right)
        #     if temp.left!=None:
        #         stack.append(temp.left)
        #Another approach
        stack=[]
        top=0
        stack.insert(top, None)
        temp=root
        # while len(stack) or temp!=None:
        while temp!=None:
            print(temp.data)
            if temp.right!=None:
                top+=1
                stack.insert(top,temp.right)
            if temp.left!=None:
                temp=temp.left
            else:
                temp=stack.pop(top)
                top-=1
    ## recursive approach
    # def preorder(self,root):
    #     res=[]
    #     if root:
    #         res.append(root.data)
    #         res= res+ self.preorder(root.left)
    #         res= res+ self.preorder(root.right)
    #     return res

    def inorder(self,root):
        stack=[]
        top=0
        stack.insert(top, None)
        temp=root
        while temp!=None:
            top+=1
            stack.insert(top,temp)
            temp=temp.left
        temp=stack.pop(top)
        top-=1
        while temp!=None:
            print(temp.data)
            temp=temp.right
            while temp!=None:
                top+=1
                stack.insert(top,temp)
                temp=temp.left
            
            temp=stack.pop(top)
            top-=1
    ## recursive approach
    # def inorder(self,root):
    #     res=[]
    #     if root:
    #         res = self.inorder(root.left)
    #         res.append(root.data)
    #         res = res + self.inorder(root.right)
    #     return res
    
    def postorder(self, root):
        if root is None:
            return

        stack1 = []
        stack2 = []

        stack1.append(root)

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            print(node.data)

    ## recursive approach
    # def postorder(self,root):
    #     res=[]
    #     if root: 
    #         res= self.postorder(root.left)
    #         res = res + self.postorder(root.right)
    #         res.append(root.data)
    #     return res

    #find value to compare compare the value with nodes
    def find(self,val):
        if val<self.data:
            if self.left!=None:
                return 
        



        

                    


e=Node(27)
e.insert(14)
e.insert(35)
e.insert(10)
e.insert(19)
e.insert(31)
e.insert(42)

e.preorder(e)
print("\n")
e.inorder(e)
print("\n")
e.postorder(e)


