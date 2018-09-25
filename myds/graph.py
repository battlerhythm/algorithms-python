class Vertex(object):
    def __init__(self, key):
        self._id = key
        self._connectedTo = {}

    def __str__(self):
        return str(self._id) + ' connectedTo: ' + str([x.id for x in self._connectedTo])

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, key):
        self._id = key

    @property
    def neighbors(self):
        return self._connectedTo.keys()
    
    def addNeighbor(self, neighbor, weight=0):
        self._connectedTo[neighbor] = weight            

    def getWeight(self, neighbor):
        return self._connectedTo[neighbor]

class Graph(object):
    def __init__(self):
        self._vrtxList = {}
        self._numVrtx = 0

    def __contains__(self, vertex):
        return vertex in self._vrtxList

    @property
    def size(self):
        return len(self.vertices), len(self.edges)

    @property
    def vertices(self):
        return self._vrtxList.keys()

    @property
    def edges(self):
        _edges = []
        for src in self._vrtxList.values():
            for dst in self._vrtxList[src.id].neighbors:
                _edges.append((src.id, dst.id))
        return _edges

    def addVertex(self, key):        
        newVertex = Vertex(key)
        self._vrtxList[key] = newVertex
        self._numVrtx += 1

    def addEdge(self, src, dst, cost=0):
        if src not in self._vrtxList:
            self.addVertex(src)
        if dst not in self._vrtxList:
            self.addVertex(dst)
        self._vrtxList[src].addNeighbor(self._vrtxList[dst], cost)