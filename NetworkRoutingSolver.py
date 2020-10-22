#!/usr/bin/python3
from ArrayPQ import Array
from HeapPQ import Heap
from CS312Graph import *
from Dijktsras import Dijkstras
import time

class NetworkRoutingSolver:
    def __init__( self):
        self.prev =[]
        pass

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network

    def getShortestPath( self, destIndex ):
        self.dest = destIndex
        path_edges = []
        total_length = 0
        index = destIndex
        if self.prev[index] is None:
            print("There is no path")
        while self.prev[index] is not None:
            currentEdge = None
            toNode = self.prev[index]
            for edge in toNode.neighbors:
                if edge.dest.node_id == index:
                    currentEdge = edge
            path_edges.append((currentEdge.dest.loc, currentEdge.src.loc, '{:.0f}'.format(currentEdge.length)))
            index = toNode.node_id

        return {'cost':total_length, 'path':path_edges}

    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex
        t1 = time.time()
        if not use_heap:
            dijkstras = Dijkstras(self.network, Array)
        else:
            dijkstras = Dijkstras(self.network, Heap)
        self.prev = dijkstras.compute(srcIndex)
        t2 = time.time()
        return (t2-t1)

