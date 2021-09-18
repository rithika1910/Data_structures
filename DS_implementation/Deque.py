class MyQueue():
    def __init__(self):
        self.f=self.node(None)
        self.r=self.node(None)
        self.sz=0
        
    class node():
        def __init__(self,data):
            self.next=None
            self.prev=None
            self.element=data
        

    def enqueue_back(self, value):
        newnode=self.node(value)
        if(self.sz==0):
            self.f=self.r=newnode
        else:
            self.r.next=newnode
            newnode.prev=self.r
            self.r=newnode
        self.sz+=1 
        self.printQueue()
        return
    
    def enqueue_front(self,value):
        newnode=self.node(value)
        if(self.sz==0):
            self.f=self.r=newnode
        else:
            self.f.prev=newnode
            newnode.next=self.f
            self.f=newnode
        self.sz+=1 
        self.printQueue()
        return
    
    def dequeue_back(self):
        if(self.sz==0):
            print("Queue Empty Exception")
            return
        elif(self.sz==1):
            self.f=None
            self.r=None
            self.sz-=1
            return
        else:
            temp=self.r.element
            curnode=self.r.prev
            curnode.next=None
            self.r.prev=None
            self.r=curnode
            self.sz-=1
        return temp

    def dequeue_front(self):
        if(self.sz==0):
            print("Queue Empty Exception")
            return
        elif(self.sz==1):
            self.f=None
            self.r=None
            self.sz-=1
            return
        else:
            temp=self.f.element
            curnode=self.f.next
            curnode.prev=None
            self.f.next=None
            self.f=curnode
            self.sz-=1
        return temp
        
    def front(self):
        return (self.f.element)
    
    def last(self):
        return (self.r.element)

    # returns True if stack is empty   
    def isEmpty(self):
        return (self.sz==0)

    # returns the number of elements currently in stack 
    def size(self):
        return (self.sz)




    def printQueue(self):
        if (self.isEmpty()):
            print("Queue Empty")
        else:
            tnode = self.f
            while tnode!= None:
                print(tnode.element,end=" ")
                tnode = tnode.next
            print()
        return

# Driver code.---------------------------------------------

def testqueue():
    q1 = MyQueue()
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(q1.size())
        elif(operation[0]=="I"):
            print(q1.isEmpty())
        elif(operation[0]=="EF"):
            q1.enqueue_front(int(operation[1]))
        elif(operation[0]=="EB"):
            q1.enqueue_back(int(operation[1]))
        elif(operation[0]=="DF"):
            print(q1.dequeue_front())
        elif(operation[0]=="DB"):
            print(q1.dequeue_back())
            q1.printQueue()
        elif(operation[0]=="F"):
            print(q1.front())
        elif(operation[0]=="DK"):
            q1.delK(int(operation[1]))
        inputs-=1

def main():
    testqueue()

if __name__ == '__main__':
    main()


