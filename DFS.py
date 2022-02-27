
##  DFS implemented using a standard looping algorithm

from data_structures.LinkedNode import LinkedNode
from data_structures.LinkedStack import LinkedStack

#   DFS algorithm
def depth_first_search(start: LinkedNode, goal: int):
    
    #   Initialize frontier as a stack
    frontier = LinkedStack()
    visited = []

    frontier.push(start)

    #   Check if graph is empty
    if start == None:
        print('Graph is empty')
        return
    
    #   Loop through all nodes
    while (frontier.size > 0):

        #   Parent is the node on the top of the stack
        parent = frontier.pop()

        #   Print parent state
        print(parent.state)
        
        #   Check parent node for goal state
        if (parent.state == goal):
            print('Goal Found')
            return

        #   Add node to visited list if not the goal
        visited.append(parent)

        #   Search through all children
        if parent.children != None:

            c_list = parent.children
            for i in range(len(c_list)):

                curr_child = c_list[len(c_list) - i - 1]

                #   Check if child node has been visited
                if (not visited.__contains__(curr_child)):

                    #   Add node to stack
                    frontier.push(curr_child)