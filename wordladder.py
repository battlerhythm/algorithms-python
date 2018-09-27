from myds.graph import Graph

grf = Graph()
grf.buildGraph('fourletterwords.txt')
grf.bfs('FOOL')
print(grf.traverse('SAGE'))
