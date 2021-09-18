class MyQueue():
    def __init__(self):
        self.f=self.node(None)
        self.r=self.node(None)
        self.sz=0
        
    class node():
        def __init__(self,data):
            self.next=None
            self.element=data
        

    def enqueue(self, value):
        newnode=self.node(value)
        if(self.sz==0):
            self.f=self.r=newnode
        else:
            self.r.next=newnode
            self.r=newnode
        self.sz+=1 
        self.printQueue()
        return
        

    def dequeue(self):
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
            self.f.next=None
            self.f=curnode
            self.sz-=1
        return temp
        
    def front(self):
        return (self.f.element)

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
        elif(operation[0]=="E"):
            q1.enqueue(int(operation[1]))
        elif(operation[0]=="D"):
            print(q1.dequeue())
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


