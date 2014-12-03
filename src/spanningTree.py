
class SpanningTree:
	def __init__(self,n):
		self.fathers = [0 for each in range(n)]
		self.distances = [0.0 for each in range(n)]
		self.maxDistance = -1
		for i in range(n):
			self.fathers[i] = -1
			self.distances[i] = -1
	def getFather(self,vertex):
		return self.fathers[vertex]
	def setFather(self,vertexA,vertexB):
		self.fathers[vertexA] = vertexB
		if vertexB >= 0:
			self.distances[vertexA] = self.distances[vertexB]+1
			if self.maxDistance == -1 or self.distances[vertexB]>self.distances[self.maxDistance]:
				self.maxDistance = vertexA
	def getMaxDistance(self):
		return self.distances[self.maxDistance]