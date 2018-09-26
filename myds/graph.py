import sys
from myds.basic import Queue

class Vertex(object):
    def __init__(self, key):
        self._id = key
        self._connectedTo = {}
        self._dist = sys.maxsize
        self._predecessor = None
        self._color = 'white'

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
    
    @property
    def distance(self):
        return self._dist

    @distance.setter
    def distance(self, newValue):
        if type(newValue) is int:
            if newValue > 0:
                self._dist = newValue
        else:
            raise TypeError("Should be positive interger include zero")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, newColor):
        if newColor in ['white', 'gray', 'black']:
            self._color = newColor
        else:
            raise ValueError('Should be \'white\', \'gray\' or \'black\'')

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

    def getVertex(self, key):
        try:
            return self._vrtxList[key]
        except KeyError:
            raise KeyError 

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

    def buildGraph(self, fileName):
        dct = {}
        with open(fileName, 'r') as f:
            for line in f:
                word = line[:-1]
                for i in range(len(word)):
                    bucket = word[:i] + '_' + word[i+1:]
                    if bucket in dct:
                        dct[bucket].append(word)
                    else:
                        dct[bucket] = [word]
        for bucket in dct.keys():
            for word1 in dct[bucket]:
                for word2 in dct[bucket]:
                    if word1 != word2:
                        self.addEdge(word1, word2)

    def bfs(self, startId):
        start = self.getVertex(startId)
        start.distance = 0
        start.predecessor = None
        vertQ = Queue()
        vertQ.enqueue(start)
        while(len(vertQ) > 0):
            currentVert = vertQ.dequeue()
            for neighbor in currentVert.neighbors:
                if(neighbor.color == 'white'):
                    neighbor.color = 'gray'
                    neighbor.distance = currentVert.distance + 1
                    neighbor.predecessor = currentVert
                    vertQ.enqueue(neighbor)
            currentVert.color = 'black'

    def traverse(self, endId):
        vertices = []
        vertex = self.getVertex(endId)
        while True:
            vertices.append(vertex.id)
            if vertex.predecessor == None:
                break
            vertex = vertex.predecessor
        return vertices
            
if __name__ == '__main__':
    grf = Graph()
    grf.buildGraph('fourletterwords.txt')
    grf.bfs('FOOL')
    print(grf.traverse('SAGE'))