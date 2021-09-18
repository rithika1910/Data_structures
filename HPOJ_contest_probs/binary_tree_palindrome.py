from collections import deque

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
        if(not (v==None)):
            self.inorderTraverse(v.leftchild)
            print(v.element,end=",")
            self.inorderTraverse(v.rightchild)
        return

    def preorderTraverse(self, v):
        if(not (v==None)):
            print(v.element,end=" ")
            self.preorderTraverse(v.leftchild)
            self.preorderTraverse(v.rightchild)
        return

    def postorderTraverse(self, v):
        if(not (v==None)):
            self.postorderTraverse(v.leftchild)
            self.postorderTraverse(v.rightchild)
            print(v.element,end=" ")
        return
    
    def preorderlist(self, v, l):
        if(not (v==None)):
            l.append(v.element)
            self.preorderlist(v.leftchild,l)
            self.preorderlist(v.rightchild,l)
        return l

    def mirror(self, v):
        if(v==None or self.isExternal(v)):
            return
        else:
            t=v.rightchild
            v.rightchild=v.leftchild
            v.leftchild=t
            self.mirror(v.leftchild)
            self.mirror(v.rightchild)
            return 
        
    def checkpalindrome(self,t1,t2):
        if(t1==t2):
            print("Is a Palindromic Tree")
        else:
            print("Is Not a Palindromic Tree")
	    
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

    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz

def main():
    tree = BinaryTree()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    nlist = tree.buildTree(arr)
    tree.postorderTraverse(tree.root)
    print()
    l=[]
    t1=tree.preorderlist(tree.root,l)
    tree.mirror(tree.root)
    tree.preorderTraverse(tree.root)
    l=[]
    t2=tree.preorderlist(tree.root,l)
    print()
    tree.checkpalindrome(t1,t2)

if __name__ == '__main__':
    main()