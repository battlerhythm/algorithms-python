from myds.basic import Queue
from myds.graph import Graph

def buildGraph(wordFile):
    dct = {}
    grf = Graph()
    with open(wordFile, 'r') as wFile:
        for line in wFile:
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
                    grf.addEdge(word1, word2)
    return grf

def bfs(graph, start):
    start.distance = 0
    start.predecessor = None
    vertQ = Queue()
    vertQ.enqueue(start)
    while(len(vertQ) > 0):
        currentVert = vertQ.dequeue()
        for neighbor in currentVert.neighbors:
            if(neighbor.color == 'white'):
                # print(neighbor.id)
                neighbor.color = 'gray'
                neighbor.distance = currentVert.distance + 1
                neighbor.predecessor = currentVert
                vertQ.enqueue(neighbor)
        currentVert.color = 'black'

def traverse(start):
    vertex = start
    while(vertex.predecessor):
        print(vertex.id)
        vertex = vertex.predecessor
    print("End",vertex.id)

wordgraph = buildGraph('fourletterwords.txt')
bfs(wordgraph, wordgraph.getVertex('FOOL'))
traverse(wordgraph.getVertex('SAGE'))




grf = Graph()
grf.buildGraph('fourletterwords.txt')
grf.bfs('FOOL')
print(grf.reverse_traverse('SAGE'))
