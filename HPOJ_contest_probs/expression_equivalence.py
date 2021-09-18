import math
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
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

    def isRoot(self,curnode):
    	if (curnode.parent==None):
    		return True
    	else:
    		return False

    def inorderTraverse(self, v):
        curnode = v
        if (curnode.leftchild != None):
            self.inorderTraverse(curnode.leftchild)
        print (curnode.element,end = ",")
        if (curnode.rightchild != None):
            self.inorderTraverse(curnode.rightchild)

    def preorderTraverse(self, v):
        curnode = v
        print(curnode.element,end=",")
        if (curnode.leftchild != None):
            self.preorderTraverse(curnode.leftchild)
        if (curnode.rightchild != None):
            self.preorderTraverse(curnode.rightchild)
        

    def postorderTraverse(self, v):
        curnode = v
        if (curnode.leftchild != None):
            self.postorderTraverse(curnode.leftchild)
        if (curnode.rightchild != None):
            self.postorderTraverse(curnode.rightchild)
        print (curnode.element,end=",")
        

    def levelorderTraverse(self, v):
        q1 = deque()
        q1.append(v)
        while (len(q1)>0):
        	temp=q1.popleft()
        	print(temp.element,end=",")
        	if temp.leftchild!=None:
        		q1.append(temp.leftchild)
        	if temp.rightchild!=None:
        		q1.append(temp.rightchild)
        return



    def buildTree(self, expr):
        #@start-editable@

        nodestack=deque()
        charstack=deque()
        precedence = {')':0,'+':1, '-':1, '*':2, '/':2}
        expr=expr.replace(" ","")
        for i in expr:
            if (i=='('):
                charstack.append(i)
            elif(i.isnumeric()):
                a=self.node()
                a.element=i
                nodestack.append(a)
            elif(precedence[i]>0):
                while(charstack and charstack[-1]!='('):
                    t= self.node()
                    t.element=charstack.pop()
                    t1=nodestack.pop()
                    t2=nodestack.pop()
                    t.leftchild=t2
                    t2.parent=t
                    t.rightchild=t1
                    t1.parent=t
                    nodestack.append(t)
                charstack.append(i)
            elif(i==')'):
                while(charstack and charstack[-1]!='('):
                    t= self.node()
                    t.element=charstack.pop()
                    t1=nodestack.pop()
                    t2=nodestack.pop()
                    t.leftchild=t2
                    t2.parent=t
                    t.rightchild=t1
                    t1.parent=t
                    nodestack.append(t)
                charstack.pop()
                
        self.root=nodestack[-1]
        nodelist=self.createnodelist(self.root)
        return nodelist
        
    def maxDepth(self,node):
        if node is None:
            return 0 ;
        else :
            lDepth = self.maxDepth(node.leftchild)
            rDepth = self.maxDepth(node.rightchild)
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1
        
    def createnodelist(self,v):
        a=self.node()
        a.element=-1
        nodes = []
        nodes.append(a)
        q1 = deque()
        q1.append(v)
        n=(2**(self.maxDepth(self.root)))-1
        z=0
        while (len(q1)>0 and z<n):
        	temp=q1.popleft()
        	nodes.append(temp)
        	if temp.leftchild!=None:
        		q1.append(temp.leftchild)
        	else:
        	    q1.append(a)
        	if temp.rightchild!=None:
        		q1.append(temp.rightchild)
        	else:
        	    q1.append(a)
        	z+=1
        return nodes	
			
        #@end-editable@
        return nodelist

    # write a function to visualize the tree

    def equivalent(self, treevec1, root1, treevec2, root2):
        #@start-editable@

        a=self.levelorderlist(root1)
        b=self.levelorderlist(root2)
        for element in a:
            try:
                b.remove(element)
            except ValueError:
                return False
        return self.evaluate(root1) == self.evaluate(root2)
        
    def levelorderlist(self, v):
        d=deque()
        l=[]
        d.append(v)
        while(len(d)>0):
            t=d.popleft()
            l.append(t.element)
            d.extend(self.getChildren(t))
        return l
        
    def evaluate(self,root):
        if root is None:
            return 0
        if root.leftchild is None and root.rightchild is None:
            return int(root.element)
        left_sum = self.evaluate(root.leftchild)
        right_sum = self.evaluate(root.rightchild)
        if root.element == '+':
            return left_sum + right_sum
        elif root.element == '-':
            return left_sum - right_sum
        elif root.element == '*':
            return left_sum * right_sum
        else:
            return left_sum / right_sum


        #@end-editable@
        

    def printTree(self, nlist):
        for i in range(len(nlist)):
            print(nlist[i].element,end=" ")
        print()


    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz


def main():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    inputs = int(input())
    while (inputs > 0):
        exp1 = input()
        exptree1 = tree1.buildTree(exp1)
        tree1.printTree(exptree1)
        exp2 = input()
        exptree2 = tree2.buildTree(exp2)
        tree2.printTree(exptree2)
        print(tree1.equivalent(exptree1, tree1.root, exptree2, tree2.root))
        inputs -= 1
 
if __name__ == '__main__':
    main()