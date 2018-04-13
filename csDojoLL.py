class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None
    def setNext(self, next):
        self.next = next
    def getNext(self):
        return self.next

head = Node(4)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(10)
nodeE = Node(2)

head.setNext(nodeB)
nodeB.setNext(nodeC)
nodeC.setNext(nodeD)
nodeD.setNext(nodeE)

def getLLLen(firstNode):
    current = firstNode
    counter = 0
    while current:
        counter += 1
        current = current.getNext()
    print(counter)

getLLLen(head)


