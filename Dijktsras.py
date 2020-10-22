import copy

from ArrayPQ import Array


class Dijkstras:
    def __init__(self, network, pqType):
        self.network = network
        self.dist = []
        self.prev = []
        self.PriorityQueue = pqType
        for i in range(len(self.network.nodes)):
            self.dist.append(float("inf"))
            self.prev.append(None)

    def compute(self, source):

        self.dist[source] = 0
        priorityQueue = self.PriorityQueue(self.dist)
        priorityQueue.makeQueue(self.network.getNodes())
        while priorityQueue.getSize() > 0:
            workingNode = priorityQueue.deleteMin()
            for edge in workingNode.neighbors:
                if self.dist[edge.dest.node_id] > self.dist[workingNode.node_id] + edge.length:
                    self.dist[edge.dest.node_id] = self.dist[workingNode.node_id] + edge.length
                    self.prev[edge.dest.node_id] = workingNode
                    priorityQueue.decreaseKey(edge.dest.node_id)

        return self.prev
