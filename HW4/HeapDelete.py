"""
Heap with added delete function
Creates and maintains a dictionary of indexes to facilitate O(1) time delete
For hashing to work the elements must be distinct
-- Cater this for Dijkstra's algorithm by handling inputs of (edge_lengeth, vertex) and having heapIndexDict track the index of the vertex
-- This involves putting '[1]' at the end of heapList entries while adding to and looking up from heapIndexDict
"""

class Heap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        self.heapIndexDict = dict()
        
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
                self.heapIndexDict[self.heapList[i // 2][1]], self.heapIndexDict[self.heapList[i][1]] = self.heapIndexDict[self.heapList[i][1]], self.heapIndexDict[self.heapList[i // 2][1]]
            i = i // 2
            
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.heapIndexDict[k[1]] = self.currentSize
        self.percUp(self.currentSize)
        
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
                self.heapIndexDict[self.heapList[i][1]], self.heapIndexDict[self.heapList[mc][1]] = self.heapIndexDict[self.heapList[mc][1]], self.heapIndexDict[self.heapList[i][1]]
            i = mc   
            
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
        
    def extractMin(self):
        retval = self.heapList[1]
        del self.heapIndexDict[self.heapList[1][1]]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapIndexDict[self.heapList[self.currentSize][1]] = 1
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
        
    def delete(self, k):
        i = self.heapIndexDict[k[1]] 
        del self.heapIndexDict[k[1]]
        self.heapList[i] = self.heapList[self.currentSize]
        if i != self.currentSize:
            self.heapIndexDict[self.heapList[self.currentSize][1]] = i
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(i)
    
    def heapify(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        for j in range(1, len(alist) + 1):
            self.heapIndexDict[self.heapList[j][1]] = j
        while (i > 0):
            self.percDown(i)
            i = i - 1
        
            
if __name__ == '__main__':
    a = [(250, 1), (300, 2), (150, 3)]
    heap = Heap()
    heap.heapify(a)
    print(heap.heapList)
    print(heap.heapIndexDict)
    print(heap.extractMin())
    print(heap.heapList)
    print(heap.heapIndexDict)
    heap.delete((250, 1))
    print(heap.heapList)
    print(heap.heapIndexDict)