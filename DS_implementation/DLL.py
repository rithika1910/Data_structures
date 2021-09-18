class DLList:
    class node:
        def __init__(self,data):
           self.element = data
           self.next = None
           self.prev = None
           
    def __init__(self):
        self.head = self.node(None)
        self.tail = self.head
        self.sz = 0
     
    def insertLast(self,u):
        temp=self.node(u)
        if(self.sz==0):
           self.tail=temp
           self.head=temp
        else:
           self.tail.next=temp
           temp.prev=self.tail
           self.tail=temp
        self.sz+=1
        return      

    def insertFirst(self,u):
        temp=self.node(u)
        if(self.sz==0):
            self.head=temp
            self.tail=temp
        else:
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
        self.sz+=1
        return
         
    #insert a node with value u after the node containing value v
    def insertAfter(self,u,v):
        temp=self.node(u)
        curnode=self.head
        tnode=self.tail
        if(tnode.element==v):
            self.insertLast(u)
            return
        while(curnode.next!= None):
            if(curnode.element==v):
                temp.next=curnode.next
                temp.prev=curnode
                curnode.next.prev=temp
                curnode.next=temp
                self.sz+=1
            curnode=curnode.next
        return

    #insert a node with value u before the node containing value v
    def insertBefore(self,u,v):
        temp=self.node(u)
        curnode=self.tail
        tnode=self.head 
        if(tnode.element==v):
            self.insertFirst(u)
            return
        while(curnode.prev!= None):
            if(curnode.element==v):
                temp.prev=curnode.prev
                temp.next=curnode
                curnode.prev=temp
                temp.prev.next=temp
                self.sz+=1 
            curnode=curnode.prev
        return

    def deleteFirst(self):
        if(self.sz==0):
            return None
        else:
            curnode=self.head.next
            curnode.prev.next=None
            curnode.prev=None
            self.head=curnode
            self.sz-=1 
        return

    def deleteLast(self):
        if(self.sz==0):
            return None
        else:
            curnode=self.tail.prev
            curnode.next.prev=None
            curnode.next=None
            self.tail=curnode
            self.sz-=1
            return

    #delete the node after the node containting value u
    def deleteAfter(self,u):
        if(self.sz==0):
            return None
        else:
            curnode=self.head
            tnode=self.tail.prev
            if(tnode.element==u):
                self.deleteLast()
                return
            while(curnode.next!=None):
                if(curnode.element==u):
                    curnode.next.next.prev=curnode
                    curnode.next=curnode.next.next
                    self.sz-=1
                curnode=curnode.next
        return

    #delete the node before the node containting value u
    def deleteBefore(self,u):
        if(self.sz==0):
            return None
        else:
            curnode=self.tail
            tnode=self.head.next
            if(tnode.element==u):
                self.deleteFirst()
                return
            while(curnode.prev!=None):
                if(curnode.element==u):
                    curnode.prev.prev.next=curnode
                    curnode.prev=curnode.prev.prev
                    self.sz-=1
                curnode=curnode.prev
        return

    def findNode(self, val):
        curnode=self.head
        while(curnode!=None):
            if(curnode.element==val):
                return val
            curnode=curnode.next
        return None

    def getHead(self):
        return self.head.element

    def getLastNode(self):
        return self.tail.element

    #swap the nodes containing u and v
    def swap(self,u,v):
        fnode=self.head
        snode=self.head
        while(fnode.element!=u):
            fnode=fnode.next
        while(snode.element!=v):
            snode=snode.next
        temp=fnode
        fnode.next=snode.next
        fnode.prev=snode.prev
        snode.prev=temp.prev
        snode.next=temp.next
        snode.prev.next=snode
        snode.next.prev=snode
        fnode.next.prev=fnode
        fnode.prev.next=fnode
        """
        #swap only values
        temp=fnode.element
        fnode.element=snode.element
        snode.element=temp
        """
        return
 
    def isEmpty(self):
        return (self.sz==0)

    def size(self):
        return self.sz

    def printList(self):
        if (self.isEmpty()):
            print ("Linked List Empty Exception")
        else:
            tnode = self.head
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.next
            print(" ")
            tnode = self.tail
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.prev
            print(" ")
        return
    
def testDLL():
    dll = DLList()
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(dll.size())
        elif(operation[0]=="I"):
            print(dll.isEmpty())
        elif(operation[0]=="IF"):
            dll.insertFirst(int(operation[1]))
            dll.printList()
        elif(operation[0]=="IL"):
            dll.insertLast(int(operation[1]))
            dll.printList()
        elif(operation[0]=="DF"):
            dll.deleteFirst()
            dll.printList()
        elif(operation[0]=="DL"):
            dll.deleteLast()
            dll.printList()
        elif(operation[0]=="IA"):
            dll.insertAfter(int(operation[1]),int(operation[2]))
            dll.printList()
        elif(operation[0]=="IB"):
            dll.insertBefore(int(operation[1]),int(operation[2]))
            dll.printList()
        elif(operation[0]=="DA"):
            dll.deleteAfter(int(operation[1]))
            dll.printList()
        elif(operation[0]=="DB"):
            dll.deleteBefore(int(operation[1]))
            dll.printList()   
        elif(operation[0]=="F"):
            print(dll.getHead())
        elif(operation[0]=='L'):
            print(dll.getLastNode())
        elif(operation[0]=='FIND'):
            print(dll.findNode(int(operation[1])))
        elif(operation[0]=='SW'):
            dll.swap(int(operation[1]),int(operation[2]))
            dll.printList()
        inputs-=1


def main():
    testDLL()

if __name__ == '__main__':
    main()

