from __future__ import annotations
from collections import deque


class Node():

    def __init__(self, data, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.data = data

    def find(self, data) -> bool:
        if data == self.data:
            return data
        elif data < self.data:
            if not self.left:
                return None
            return self.left.find(data)
        else:
            if not self.right:
                return None
            return self.right.find(data)

    def insert(self, data) -> bool:
        if data == self.data:
            return False
        elif data < self.data:
            if not self.left:
                self.left = Node(data, self)
                return True
            return self.left.insert(data)
        else:
            if not self.right:
                self.right = Node(data, self)
                return True
            return self.right.insert(data)

    """
    def rama(self, to_replace) -> Node:
        if self.right:
            self.right.rama(to_replace)
        else:
            self.parent.right = self.left
            return self

    def remove(self, data) -> bool:
        if data == self.data:
            if self.left and self.right:
                if self.parent.left == self.left:
                    self.parent.left = self.left.rarm(self)
                    self = self.parent.left
                else:
                    self.parent.right = self.right.rarm(self)
                    self = self.parent.right
            elif self.left:
                if self == self.parent.left:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
            else:
                if self == self.parent.left:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
        elif data < self.data:
            if not self.left:
                return False
            else:
                return self.left.remove(data)
        else:
            if not self.remove:
                return False
            else:
                return self.remove.remove(data)
    """
    """
    def rarm(self, pip):
        if self.left:
            return self.left.rarm(self.left)
        else:
            pip = self.left
            return self

    def remove(self, data, pip):
        if data == self.data:
            if self.left and self.right:
                node = self.right.rarm(self.right)
                pip = node
                node.left = self.left
                node.right = self.right
            elif self.left:
                pip = self.left
                return data
            elif self.right:
                pip = self.right
                return data
            else:
                pip = None
                return data

        elif data < self.data:
            if self.left:
                return self.left.remove(data, self.left)
            else:
                return None
        else:
            if self.right:
                return self.right.remove(data, self.right)
            else:
                return None
    """
    def write(self):
        print(self.data)
        if self.left:
            self.left.write()
        if self.right:
            self.right.write()


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
            self.root = Node(data, self.root)
            return True
        else:
            return self.root.insert(data)

    def remove(self, data):
        if self.root:
            data = self.root.remove(data)
            return data
        else:
            return None

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return None

    def write_tree(self):
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
    # print('Testing remove ======')
    # print(tree.remove(2))
    # tree.write_tree()
    # print('===================\n')
