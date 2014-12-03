import sys, os, unittest

#CURRENT_PATH = os.path.dirname(os.path.abspath('__file__'))
#sys.path.append(CURRENT_PATH + '/../lib')

from ..listStorage import ListStorage
from ..matrixStorage import MatrixStorage

class BaseTestGraph:
	def addEdges(self):
		self.graph.addEdge(0,1)
		self.graph.addEdge(0,2)
		self.graph.addEdge(0,2)
		self.graph.addEdge(2,3)
		self.graph.addEdge(2,4)
		self.graph.addEdge(3,4)

	def testDegree(self):
		self.assertEqual(self.graph.getDegree(2), 3)
	def testNeighbors(self):
		self.assertEqual(len(self.graph.getNeighbors(2)), 3)
	def testNodeCount(self):
		self.assertEqual(self.graph.getNodeCount(), 5)
	def testIsNeighbor(self):
		self.assertTrue(self.graph.isNeighbor(0,1))
		self.assertFalse(self.graph.isNeighbor(0,3))

class TestMatrix(unittest.TestCase, BaseTestGraph):
	def setUp(self):
		self.graph = MatrixStorage(5)
		self.addEdges()

class TestList(unittest.TestCase, BaseTestGraph):
	def setUp(self):
		self.graph = ListStorage(5)
		self.addEdges()

if __name__ == '__main__':
	unittest.main()