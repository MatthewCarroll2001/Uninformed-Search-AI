
##  Linked Node for use in Linked List

from inspect import _void
from typing import List

class LinkedNode():
    state: int
    next: _void
    children: List[_void]

    def __init__(self, state: int):
        self.state = state
        self.next = None
        self.children = None