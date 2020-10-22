class Heap:
    def __init__(self, key):
        self.priorityQueue = []
        self.distKey = key
        self.pointer =[]
        self.size =0

    def swap(self,parent,child):
        self.priorityQueue[parent], self.priorityQueue[child] = self.priorityQueue[child], self.priorityQueue[parent]

    # O(nlog(v)) because it only compares to children for each insert on a binary tree
    def makeQueue(self, nodes):
        for node in nodes:
            self.insert(node)

    # O(log(v)) because it only compares to parents on a binary tree
    def insert(self, node):

        self.priorityQueue.append(node)

        currIndex = self.size
        self.pointer.append(currIndex)
        while self.distKey[self.priorityQueue[currIndex].node_id] < self.distKey[self.priorityQueue[int((currIndex-1)/2)].node_id]:
            self.swap(int((currIndex-1)/2), currIndex)
            currIndex = int((currIndex-1)/2)
        self.size += 1
        self.pointer[node.node_id] = currIndex

    # O(1)
    def twoChildSink(self, currIndex):
        leftChildValue = self.distKey[self.priorityQueue[int((currIndex * 2) + 1)].node_id]
        rightChildValue = self.distKey[self.priorityQueue[int((currIndex * 2) + 2)].node_id]

        if self.distKey[self.priorityQueue[currIndex].node_id] > leftChildValue or self.distKey[self.priorityQueue[currIndex].node_id] > rightChildValue:
            if (leftChildValue < rightChildValue):  # bubble up smaller child
                self.pointer[self.priorityQueue[currIndex].node_id], self.pointer[
                    self.priorityQueue[int((currIndex * 2) + 1)].node_id] = self.pointer[self.priorityQueue[
                    int((currIndex * 2) + 1)].node_id], self.pointer[self.priorityQueue[currIndex].node_id]
                self.swap(currIndex, int((currIndex * 2) + 1))
                currIndex = int((currIndex * 2) + 1)
            else:
                self.pointer[self.priorityQueue[currIndex].node_id], self.pointer[
                    self.priorityQueue[int((currIndex * 2) + 2)].node_id] = self.pointer[self.priorityQueue[
                    int((currIndex * 2) + 2)].node_id], self.pointer[self.priorityQueue[currIndex].node_id]
                self.swap(currIndex, int((currIndex * 2) + 2))
                currIndex = int((currIndex * 2) + 2)

            return currIndex
    #O(1)
    def oneChildSink(self, currIndex):
        leftChildValue = self.distKey[self.priorityQueue[int((currIndex * 2) + 1)].node_id]

        if self.distKey[self.priorityQueue[currIndex].node_id] > leftChildValue:
            self.pointer[self.priorityQueue[currIndex].node_id], self.pointer[
                    self.priorityQueue[int((currIndex * 2) + 1)].node_id] = self.pointer[self.priorityQueue[
                    int((currIndex * 2) + 1)].node_id], self.pointer[self.priorityQueue[currIndex].node_id]
            self.swap(currIndex, int((currIndex * 2) + 1))
            currIndex = int((currIndex * 2) + 1)

            return currIndex

    # O(log(v)) because it only compares to children on a binary tree
    def deleteMin(self):
        nodeToReturn = self.priorityQueue[0]

        self.priorityQueue[0] = self.priorityQueue[self.size-1]
        self.pointer[self.priorityQueue[0].node_id] = 0
        self.pointer[nodeToReturn.node_id] = None
        self.priorityQueue.pop()

        self.size -= 1
        currIndex = 0
        while currIndex != None and int((currIndex*2) + 1) < self.size:
            if int((currIndex*2) + 2) < self.size:
                currIndex = self.twoChildSink(currIndex)
            else:
                currIndex = self.oneChildSink(currIndex)

        return nodeToReturn

    #O(log(v)) because it only compares to parent on a binary tree
    def decreaseKey(self, index):
        currIndex = self.pointer[index]

        while self.distKey[self.priorityQueue[currIndex].node_id] < self.distKey[self.priorityQueue[int((currIndex - 1) / 2)].node_id]:
            self.swap(int((currIndex - 1) / 2), currIndex)

            self.pointer[self.priorityQueue[currIndex].node_id], self.pointer[
                self.priorityQueue[int((currIndex -1) / 2)].node_id] = self.pointer[self.priorityQueue[
                int((currIndex -1) / 2)].node_id], self.pointer[self.priorityQueue[currIndex].node_id]
            currIndex = int((currIndex - 1) / 2)


    def getSize(self):
        return self.size

