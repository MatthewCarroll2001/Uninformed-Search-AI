
##  Implementation of a traditional stack with linked nodes

from data_structures.LinkedNode import LinkedNode

class LinkedStack:
    top: LinkedNode
    size: int

    def __init__(self):
        self.size = 0

    def push(self, node: LinkedNode):
        if self.size == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node

        self.size += 1

    def pop(self) -> LinkedNode:
        if self.size == 0:
            print('Stack empty')
            return None
        
        temp = self.top
        self.top = self.top.next

        self.size -= 1

        return temp