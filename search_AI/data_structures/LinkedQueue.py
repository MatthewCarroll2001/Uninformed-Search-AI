
##  Simple implementation of a Linked List for the purposes of searching

from data_structures import LinkedNode

class LinkedQueue:
    start: LinkedNode
    end: LinkedNode
    size: int

    def __init__(self):
        self.size = 0
        self.start = None
        self.end = None

    def enqueue(self, node: LinkedNode):
        if self.size == 0:
            self.start = node
        else:
            self.end.next = node
        
        self.end = node
        self.size += 1

    def dequeue(self) -> LinkedNode:
        temp = self.start
        self.start = self.start.next
        self.size -= 1

        return temp

    def __str__(self):
        curr = self.start
        while curr != None:
            print(curr.state)
            curr = curr.next