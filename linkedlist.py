#singly linked list

class singlylinkedlist:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

head = singlylinkedlist(1) #head node with a value of 1 contained in the node.

#make the next nodes
node1 = singlylinkedlist(5)
node2 = singlylinkedlist(10)
node3 = singlylinkedlist(15)

#connect the nodes together
head.next = node1
node1.next = node2
node2.next = node3
#node3.next = None not needed

print(head.data)





