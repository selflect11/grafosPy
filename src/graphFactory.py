from graph import Graph

class GraphFactory:
	def __init__(self, path, Storage):
		try:
			with open(path,'r') as f:
				#pega a primeira linha
				G = Graph(int(f.readline()), Storage)
				#pega as linhas restantes
				#adiciona as arestas
				for line in f:
					G.edgeCount += 1
					#nossa indexação começa em zero
					#subtrair 1 daqui
					i,j = map(lambda k: int(k) - 1, line.split(" "))
					G.Storage.addEdge(i,j)
		except (Exception, e):
			print(e)
