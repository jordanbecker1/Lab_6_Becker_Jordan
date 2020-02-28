class Node:
	def __init__(self,data,nextPointer = None):
		self.data = data
		self.nextPointer = nextPointer

	def getData(self):
		return(self.data)

	def setData(self, ndata):
		self.data = ndata

	def getnextPointer(self):
		return(self.nextPointer)

	def setnextPointer(self, n):
		self.nextPointer = n

def main():
	n = Node(data = 100)

	print(n.setData("AU"))

if __name__ == '__main__':
	main()
