import numpy as np

class MatrixStorage:
	def __init__(self,n):
		self.adjacencyMatrix = np.zeros((n,n),dtype=float)

	def addEdge(self,i,j,w=1):
		if self.isNeighbor(i,j) or i==j:
			return None
		self.adjacencyMatrix[i][j] = w

	def getNeighbors(self,vertex):
		neighbors = np.array([],dtype=int)
		for j in range(self.getNodeCount()):
			if self.isNeighbor(i,j):
				neighbors = np.append(neighbors,j)
		return neighbors

	def isNeighbor(self,i,j):
		#ta serto?
		return (self.adjacencyMatrix[i][j] or self.adjacencyMatrix[j][i])

	def getDegree(self,vertex):
		degree = 0
		for j in range(self.getNodeCount()):
			if self.isNeighbor(i,j):
				degree += 1
		return degree