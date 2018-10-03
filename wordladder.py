from myds.graph import BFSGraph

grf = BFSGraph()
grf.buildGraph('fourletterwords.txt')
grf.bfs('FOOL')
print(grf.traverse('SAGE'))
