import math
class BinarySearchTree:
    
    class node:
        def __init__(self,data):
            self.element = data
            self.leftchild = None
            self.rightchild = None
            self.pos = -1
            self.parent = None

    def __init__(self):
        self.size = 0
        self.root = None
        self.ht = 0

    
    def insertP(self,e,v):
        if(v==None):
            v= self.node(e)
            self.root=v
        elif(e<=v.element):
            if(v.leftchild==None):
                v.leftchild= self.node(e)
            else:
                self.insertP(e,v.leftchild)
        elif(e>v.element):
            if(v.rightchild==None):
                v.rightchild= self.node(e)
            else:
                self.insertP(e,v.rightchild)
        return
    
    def hundredPercentile(self,v):
        current = v
        while(current.rightchild):
            current = current.rightchild
        return current.element
        
    def percGreater(self,k,v):
        l=[]
        pl=self.Percentilelist(v)
        for p in pl:
            if(p>k):
                l.append(p)
        return len(l)
            
    def preorderTraverse(self,v):
        curnode = v
        print (curnode.element,end=" ")
        if (curnode.leftchild != None):
            self.preorderTraverse(curnode.leftchild)
        if (curnode.rightchild!=None):
            self.preorderTraverse(curnode.rightchild)
        return

    def Percentilelist(self,v):
        p=[]
        l=[]
        l=self.inorderlist(self.root,l)
        for i in l:
            r=l.index(i)+1
            p.append(int(math.ceil((r*100)/len(l))))
        return p
    
    def inorderlist(self,v,l):
        curnode = v
        if (curnode.leftchild != None):
            self.inorderlist(curnode.leftchild,l)
        l.append(curnode.element)
        if (curnode.rightchild!=None):
            self.inorderlist(curnode.rightchild,l)
        return l
        
    def getPercentile(self,k):
        l=[]
        l=self.inorderlist(self.root,l)
        r=l.index(k)+1
        return (int(math.ceil((r*100)/len(l))))

def testbst():
    ds = BinarySearchTree()
    inputs = int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="H"):
            print(ds.hundredPercentile(ds.root))
        elif(operation[0]=="I"):
            ds.insertP(int(operation[1]),ds.root)
            ds.preorderTraverse(ds.root)
            print()
        elif(operation[0]=="G"):
            print(ds.percGreater(int(operation[1]),ds.root))
        elif(operation[0]=="P"):
            print(ds.getPercentile(int(operation[1])))
        inputs-=1

def main():
    testbst()

if __name__ == '__main__':
    main()