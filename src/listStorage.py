import numpy as np

class ListStorage:
	def __init__(self,n):
		self.adjacencyList = [[] for each in range(n)]
		
	def addEdge(self,i,j,w=1):
		if self.isNeighbor(i,j) or i==j:
			return None
		self.adjacencyList[i].append(j)
		self.adjacencyList[j].append(i)

	def getNeighbors(self,vertex):
		return self.adjacencyList[vertex]

	def isNeighbor(self,i,j):
		for each in self.adjacencyList[i]:
			if each == j:
				return True
		return False

	def getDegree(self,vertex):
		return len(self.adjacencyList[vertex])
