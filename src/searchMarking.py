#depois eu jogo pra outro arquivo isso::
global mark = {'undiscovered':-1, 'discovered':0,'explored':1}


class SearchMarking:
	def __init__(self,n):
		self.marks = [0 for each in range(n)]
		self.count = n
	def set(self,vertex,mark):
		self.marks[vertex] = mark
	def setAll(self, mark):
		for i in range(self.count):
			self.set(i,mark)
	def markIs(self,vertex,mark):
		return self.marks[vertex] == mark;