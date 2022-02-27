
##  Depth-First Search finds deepest path first starting in the leftmost path
##  This version is a recursive implementation

from data_structures.LinkedNode import LinkedNode

#   Initial DFS function call
def DFS_Recursive_Initial(start: LinkedNode, goal: int):
    
    #   Check first node to make sure graph is not empty
    if start == None:
        print('Graph is empty')
        return

    #   Initial recursive call
    DFS_Recursive(start, goal)

#   Recursive function that traverses the graph using DFS method
def DFS_Recursive(node: LinkedNode, goal: int):

    #   If node is null somehow, return it
    if node == None:
        return

    #   Print current node state and check for goal state
    print(node.state)
    if node.state == goal:
        print('Goal Found')
        return

    #   Repeat function for all children
    if node.children != None:
        for child in node.children:
            DFS_Recursive(child, goal)