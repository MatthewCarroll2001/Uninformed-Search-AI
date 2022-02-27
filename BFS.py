
##  Breadth-First Search searches all nodes of a specific depth before moving onto the next set of expanded nodes

from data_structures.LinkedQueue import LinkedQueue
from data_structures.LinkedNode import LinkedNode

def breadth_first_search(start: LinkedNode,  goal: int):
    
    #   Instantiate frontier and visited lists
    frontier = LinkedQueue()
    visited = []

    #   Put first node in frontier
    frontier.enqueue(start)

    #   Check initial node for goal state
    print(start.state)
    if (start.state == goal):
        print('Goal Found')
        return

    #   Search until frontier has no more nodes to check
    while (frontier.size > 0):

        #   Dequeue first element
        parent = frontier.dequeue()

        #   Loop through all children
        for child in parent.children:

            #   Check if child has been visited
            if (not visited.__contains__(child)):
                
                #   Print child data and enqueue that child
                print(child.state)
                frontier.enqueue(child)

                #   Check child for goal state
                if (child.state == goal):
                    print('Goal Found')
                    return
                else:
                    visited.append(child)