from Node import Node

class LinkedList():
	def __init__(self, head = None, size = 0, tail = 1):
		self.head = head
		self.size = size
		self.tail = tail

	def getHead(self):
		return(self.head)

	def setHead(self, head1):
		self.head = head1

	def getSize(self):
		return(self.size)

	def setSize(self, n):
		self.size = n

	def getTail(self):
		return(self.tail)

	def setTail(self, ntail):
		self.tail = ntail

	def isEmpty(self):
		if(self.getSize() > 0):
			return(False)
		return(True)

	def addNode(self, d):
		newNode = Node(data = d)


		if(self.isEmpty()):
			self.setHead(newNode)

		else:
			
			self.getTail().setnextPointer(newNode)

		self.setTail(newNode)
		self.setSize(self.size + 1)


def main():
	ll = LinkedList()
	ll.addNode(1000)

	ll.addNode(1000)

	ll.addNode("Cheddar")

	print(ll.getTail().getData())


if __name__ == '__main__':
	main()