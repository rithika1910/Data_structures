class MyStack():
    def __init__(self,size):
        self.sz=size
        self.cursz=0
        self.head=self.node(None)
        self.tail=self.node(None)
    
    class node():
        def __init__(self,element):
            self.element=element
            self.next=None

    # define the push operation which  pushes the value into the stack, must throw a stack full exception
    def push(self, value):
        temp=self.node(value)
        if(self.cursz==0):
            self.tail=temp
            self.head=temp
        elif(self.sz==self.cursz):
            print("stack full exception")
            return
        else:
            self.tail.next=temp
            self.tail=temp
        self.cursz+=1
        return
        

    # returns top element of stack if not empty, else throws stack empty exception
    def pop(self):
        if(self.cursz==0):
            return print("stack empty exception")
        elif(self.cursz==1):
            temp=self.head.element
            self.tail=None
            self.head=None
            self.cursz=0
        else:
            curnode=self.head
            temp=self.tail.element
            while(curnode.next.next!=None):
                curnode=curnode.next
            self.tail=curnode
            self.tail.next=None
            self.cursz-=1
        return temp
        
    # returns top element without removing it if the stack is not empty, else throws exception   
    def top(self):
        if(self.cursz==0):
            print("stack empty exception")
            return
        else:
            return (self.tail.element)

    # returns True if stack is empty   
    def isEmpty(self):
        return (self.cursz==0)

    # returns the number of elements currently in stack 
    def size(self):
        return (self.cursz)




    def printStack(self):
        if (self.isEmpty()):
            print("Empty")
        else:
            tnode=self.head
            while (tnode!=None):
                print(tnode.element,end="->")
                tnode=tnode.next
            print(" ")
        return

# Driver code.---------------------------------------------

def teststack():
    stacksize=int(input())
    st1 = MyStack(stacksize)
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(st1.size())
        elif(operation[0]=="I"):
            print(st1.isEmpty())
        elif(operation[0]=="P"):
            st1.push(int(operation[1]))
            st1.printStack()
        elif(operation[0]=="O"):
            print(st1.pop())
            st1.printStack()
        elif(operation[0]=="T"):
            print(st1.top())
            st1.printStack()
        inputs-=1

def main():
    teststack()

if __name__ == '__main__':
    main()

