#@start-editable@

from collections import deque
		
			
#@end-editable@

class BinaryTree:
    class node:
        def __init__(self):
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None
            

    def __init__(self):
        self.sz = 0
        self.root = self.node()
        self.ht = 0
        

    def getChildren(self, curnode):
        children = []
        if curnode.leftchild != None:
            children.append(curnode.leftchild)
        if curnode.rightchild != None:
            children.append(curnode.rightchild)
        return children

    def isExternal(self, curnode):
        if (curnode.leftchild==None and curnode.rightchild==None):
            return (True)
        else:
            return (False)

    def isRoot(self,curnode):
        if (curnode.parent==None):
            return True
        else:
            return False   	

    def inorderTraverse(self, v):
        #@start-editable@

        if(not (v==None)):
            self.inorderTraverse(v.leftchild)
            print(v.element,end=",")
            self.inorderTraverse(v.rightchild)
        return
			
			
	    #@end-editable@
        

    def preorderTraverse(self, v):
        #@start-editable@

        if(not (v==None)):
            print(v.element,end=",")
            self.preorderTraverse(v.leftchild)
            self.preorderTraverse(v.rightchild)
        return
			
			
	    #@end-editable@
       

    def postorderTraverse(self, v):
        #@start-editable@

        if(not (v==None)):
            self.postorderTraverse(v.leftchild)
            self.postorderTraverse(v.rightchild)
            print(v.element,end=",")
        return
			
			
	    #@end-editable@
        

    def levelorderTraverse(self, v):
        #@start-editable@

        d=deque()
        d.append(v)
        while(len(d)>0):
            t=d.popleft()
            print(t.element,end=",")
            d.extend(self.getChildren(t))
			
			
	    #@end-editable@
       

    def findDepth(self, v):
        #@start-editable@

        depth=0
        n=self.root
        while(not (n==v)):
            depth+=1
            v=v.parent
        return depth
			
			
	    #@end-editable@
    	

    def findHeight(self, v):
        #@start-editable@

        if(self.isExternal(v)):
            return 0
        else:
            h=0
            for nodes in self.getChildren(v):
                h=self.findHeight(nodes)
        return h+1
			
			
	    #@end-editable@
    	

    # delete leaves in the tree
    def delLeaves(self, v):
        #@start-editable@


        if(v==None or self.isExternal(v)):
            return None
        else:
            v.leftchild=self.delLeaves(v.leftchild)
            v.rightchild=self.delLeaves(v.rightchild)
            return v
			
			
	    #@end-editable@
        
    # returns true if tree is proper
    def isProper(self, v):
        #@start-editable@

        if(self.isExternal(v)):
            return True
        elif(not (v.leftchild==None) and not (v.rightchild==None)):
            return (self.isProper(v.leftchild) and self.isProper(v.rightchild))
        else:
            return False
			
			
	    #@end-editable@
        
    # create a tree that is a mirror image of the original tree and print its levelorder
    def mirror(self, v):
        #@start-editable@

        if(v==None or self.isExternal(v)):
            return
        else:
            t=v.rightchild
            v.rightchild=v.leftchild
            v.leftchild=t
            self.mirror(v.leftchild)
            self.mirror(v.rightchild)
            return 
			
			
	    #@end-editable@
        

    def buildTree(self, eltlist):
        nodelist = []
        nodelist.append(None)
        for i in range(len(eltlist)):
            if (i != 0):
                if (eltlist[i] != -1):
                    tempnode = self.node()
                    tempnode.element = eltlist[i]
                    if i != 1:
                        tempnode.parent = nodelist[i // 2]
                        if (i % 2 == 0):
                            nodelist[i // 2].leftchild = tempnode
                        else:
                            nodelist[i // 2].rightchild = tempnode
                    nodelist.append(tempnode)
                else:
                    nodelist.append(None)

        self.root = nodelist[1]
        self.sz=len(nodelist)
        return nodelist

    # write a function to visualize the tree

    def printTree(self, nlist):
        for i in range(len(nlist)):
            if (nlist[i] != None):
                print(nlist[i].element,end=" ");
            else:
                print(None)


    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz

    #determine whether there exists a root-to-leaf path whose nodes sum is equal to a specified integer
    def root2leafsum(self, k):
        #@start-editable@

        v=self.root
        list=[]
        list=self.findsum(v,0,list)
        for n in list:
            if(n==k):
                print("True")
                return
        print("False")
        return
        
    def findsum(self,v,sum,l):
        if(v==None):
            return 
        if(self.isExternal(v)):
            sum=sum+v.element
            l.append(sum)
            return
        else:
            sum=sum+v.element
            self.findsum(v.leftchild,sum,l)
            self.findsum(v.rightchild,sum,l)
        return l
        
			
			
	    #@end-editable@
        

    #determine the value of the leaf node in a given binary tree that is the terminal node of a path of least value from the root of the binary tree to any leaf. The value of a path is the sum of values of nodes along that path.
    def leastleaf(self):
        #@start-editable@

        l=[]
        s=[]
        sum=0
        v=self.root
        self.least(v,l,s,sum)
        min_sum=s[0]
        c=0
        t=0
        for e in s:
            if(min_sum>e):
                min_sum=e
                t=c
                break
            c+=1
        min_leaf=l[t]
        print(min_leaf)
        return
    
    def least(self,v,l,s,sum):
        if(v==None):
            return 
        if(self.isExternal(v)):
            sum=sum+v.element
            l.append(v.element)
            s.append(sum)
            return
        else:
            sum=sum+v.element
            self.least(v.leftchild,l,s,sum)
            self.least(v.rightchild,l,s,sum)
        return
			
			
	    #@end-editable@
        

def main():
    tree = BinaryTree()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    nlist = tree.buildTree(arr)
    inputs = int(input())
    while inputs > 0:
         command = input()
         operation = command.split()
         if (operation[0] == "I"):
              tree.inorderTraverse(tree.root)
              print()
         elif (operation[0] == "P"):
              tree.preorderTraverse(tree.root)
              print()
         elif (operation[0] == "Post"):
              tree.postorderTraverse(tree.root)
              print()
         elif (operation[0] == "L"):
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == "D"):
              pos = int(operation[1])
              print(tree.findDepth(nlist[pos]))
         elif (operation[0] == "H"):
              pos = int(operation[1])
              print(tree.findHeight(nlist[pos]))
         elif (operation[0] == "IP"):
              print(tree.isProper(tree.root))
         elif (operation[0] == 'M'):
              tree.mirror(tree.root)
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == 'DL'):
              tree.delLeaves(tree.root)
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == 'RL'):
              tree.root2leafsum(int(operation[1]))
              print()
         elif (operation[0] == 'ML'):
              tree.leastleaf()
              print()
         inputs -= 1

if __name__ == '__main__':
    main()