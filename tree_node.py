class Node:
    """
    The data that being stored in the node should have
    __lt__, __gt__, __eq__ functions being implemented.
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data) -> bool:
        if self.data == data:
            return False
        elif self.data < data:
            if not self.left:
                self.left = Node(data)
                return True
            else:
                return self.left.insert(data)
        else:
            if not self.right:
                self.right = Node(data)
                return True
            else:
                return self.right.insert(data)

    def find(self, data) -> bool:
        if self.data == data:
            return False
        elif self.data < data:
            if not self.left:
                return False
            else:
                return self.left.find(data)
        else:
            if not self.right:
                return False
            else:
                return self.right.find(data)
