class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    """ This method defines the upheap function when inserting an element
    """
    def upHeapp(self,i):
        #@start-editable@

        while(i>1):
            if(self.heapList[i//2]>self.heapList[i]):
                t=self.heapList[i]
                self.heapList[i]=self.heapList[i//2]
                self.heapList[i//2]=t
            i-=1   
			
	    #@end-editable@
            
    def insert(self,k):
        #@start-editable@

        self.heapList.append(k)
        self.currentSize+=1
        self.upHeapp(self.currentSize)
			
	    #@end-editable@

    """ This method defines the downheap function when removing min
    """
    def downHeap(self,i):
        #@start-editable@

        while((i*2)<self.currentSize):
            m=self.minChild(i)
            if(self.heapList[m]<self.heapList[i]):
                t=self.heapList[m]
                self.heapList[m]=self.heapList[i]
                self.heapList[i]=t
            i=m	
			
	    #@end-editable@

    def minChild(self,i):
        #@start-editable@

        if (((i*2)+1)>self.currentSize or self.heapList[(i*2)+1]>self.heapList[(i*2)]):
            return (i*2)
        else:
            return (i*2)+1
            
	    #@end-editable@

    def delMin(self):
        #@start-editable@

        self.heapList[1]=self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize-=1
        self.downHeap(1)
        
			
	    #@end-editable@
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):  #// \label{lst:bh:loop}
            self.downHeap(i)
            i = i - 1


    #create a method to print the contents of the heap in level order 
    def printHeap(self):
        print(self.heapList)

def main():
    heap = BinHeap()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    heap.buildHeap(arr)
    inputs = int(input())
    while inputs > 0:
         command = input()
         operation = command.split()
         if (operation[0] == "I"):
              heap.insert(int(operation[1]))
              heap.printHeap()
         elif (operation[0] == "R"):
              heap.delMin()
              heap.printHeap()
         inputs -= 1

if __name__ == '__main__':
    main()