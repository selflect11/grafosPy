class Graph:
	def __init__(self, n, Storage):
		self.edgeCount = 0
		self.nodeCount = n
		self.Storage = Storage(self.nodeCount)

	def getNodeCount(self):
		return self.nodeCount

	def getEdgeCount(self):
		return self.edgeCount

	def getAverageDegree(self):
		pass

	def getEmpiricDistrib(self):
		pass