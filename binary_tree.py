from __future__ import annotations
from collections import deque

from tree_node import Node


class BinaryTree():
    """
    The type of data being stored must have __lt__ and __eq__ function
    """

    def __init__(self):
        self.num_of_nodes = 0
        self.root = None

    def insert(self, data):
        """
        No duplicates is allowed
        """
        if not self.root:
            self.root = Node(data)
            return True
        else:
            return self.root.insert(data)

    def find(self, data) -> bool:
        if self.root:
            return self.root.find(data)
        else:
            return False

    def remove(self, data) -> bool:
        if self.root is None:  # when the tree is empty
            return False
        if self.root.data == data:  # remove the root
            if self.root.left is None and self.root.right is None:
                self.root = None
                return True
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
                return True
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
                return True
            else:  # replace and remove max
                moveNode = self.root.right
                moveNodeParent = None
                while moveNode.left:
                    moveNodeParent = moveNode
                    moveNode = moveNode.left
                    self.root.data = moveNode.data
                    if moveNode.data < moveNodeParent.data:
                        moveNodeParent.left = None
                    else:
                        moveNodeParent.right = None
                    return True
        # remove a regular node
        parent = None
        direction = 0
        curr = self.root
        while curr.data != data:
            parent = curr
            if curr.data < data:
                curr = curr.left
                direction = -1
                if curr is None:
                    return False
            else:
                curr = curr.right
                direction = 1
                if curr is None:
                    return False

        if curr.left is None and curr.right is None:
            if direction > 0:
                parent.right = None
            else:
                parent.left = None
        elif curr.left is None and curr.right:
            if direction > 0:
                parent.right = curr.right
            else:
                parent.left = curr.right
        elif curr.left and curr.right is None:
            if direction > 0:
                parent.right = curr.left
            else:
                parent.left = curr.left
        else:  # replace and remove max
            moveNodeParent = curr
            moveNode = curr.right
            while moveNode.left:
                moveNodeParent = moveNode
                moveNode = moveNode.left
            curr.data = moveNode.data
            if moveNode.right:
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = moveNode.right
                else:
                    moveNodeParent.right = moveNode.right
            else:
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = None
                else:
                    moveNodeParent.right = None
        return True

    def write_tree(self):
        if self.root:
            self.root.write()

    def bfs(self):
        ret = []
        if self.root is None:
            return ret
        dq = deque()
        dq.append(self.root)
        while len(dq) > 0:
            curr_level = []
            for i in range(len(dq)):
                curr_node = dq.popleft()
                curr_level.append(curr_node.data)
                if curr_node.left:
                    dq.append(curr_node.left)
                if curr_node.right:
                    dq.append(curr_node.right)
            ret.append(curr_level)
        return ret

    def write_level_order(self):
        levels = self.bfs()
        for i in range(len(levels)):
            print("Level " + str(i) + " : " + str(levels[i]))


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    print('Testing find ======')
    print(tree.find(2))
    print('===================\n')
    tree.write_tree()
    tree = BinaryTree()
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)
    tree.write_tree()
    print(tree.write_level_order())
    tree.remove(2)
    tree.write_tree()
    print('Testing remove ======')
    print(tree.remove(2))
    tree.write_tree()
    print('===================\n')
