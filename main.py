
##  Environment for creating graphs and searching them for solutions

from logging import root
from DFS import depth_first_search
from DFS_Recursive import DFS_Recursive_Initial
from data_structures.LinkedNode import LinkedNode
from BFS import breadth_first_search

def main():
    #   Create root and subsequent depths
    root = LinkedNode(1)
    depth_1 = [LinkedNode(2), LinkedNode(3)]
    depth_2 = [[LinkedNode(4), LinkedNode(5)], [LinkedNode(6), LinkedNode(7)]]

    #   Assign children to all nodes
    root.children = depth_1
    root.children[0].children = depth_2[0]
    root.children[1].children = depth_2[1]

    #   BFS
    print('BFS:')
    breadth_first_search(root, 7)

    #   DFS Standard
    print('DFS:')
    depth_first_search(root, 7)

    #   DFS Recursive
    print('DFS Recursive:')
    DFS_Recursive_Initial(root, 7)

if __name__ == '__main__':
    main()