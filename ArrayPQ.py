class Array:
    def __init__(self, key):
        self.priorityQueue = []
        self.key = key
    #O(n) because 1 for each node
    def makeQueue(self, nodes):
        for node in nodes:
            self.insert(node)

    #O(1)
    def insert(self, node):
        self.priorityQueue.append(node)

    #O(n) because it must search through the whole list
    def deleteMin(self):
        minIndex = 0
        keyMin = self.priorityQueue[0].node_id
        for i in range(len(self.priorityQueue)):
            keyIndex = self.priorityQueue[i].node_id
            if self.key[keyMin] > self.key[keyIndex]:
                minIndex = i
                keyMin = keyIndex
        return self.priorityQueue.pop(minIndex)

    #O(1) because it does absolutely nothing
    def decreaseKey(self, index):
        pass
        #because it is passing by reference it does not need updated

    #O(1) for finding the length according to the internet
    def getSize(self):
        return len(self.priorityQueue)
