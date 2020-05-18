from heapq import heappush, heappop


class Node():
    def __init__(self, data, count):
        self.data = data
        self.count = count
        self.left = None
        self.right = None
        self.parent = None

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Node):
            return str(self.data) < str(other.data)
        else:
            return False


class Huffman_Tree:

    def __init__(self, s_to_encode):
        self.root = None 
        self.leaf_list = None
        c_count = {}
        for char in s_to_encode:
            if char in c_count:
                c_count[char] += 1
            else:
                c_count[char] = 0
        char_count_list = [(k, v) for k, v in c_count.items()]
        self.build_tree(char_count_list)

    def build_tree(self, char_count_list):
        node_pq = []
        for pair in char_count_list:
            node = Node(pair[0], pair[1])
            heappush(node_pq, (node.count, node))
        self.leaf_list = []

        for _, node in node_pq:
            self.leaf_list.append(node)

        while len(node_pq) > 1:
            _, left = heappop(node_pq)
            _, right = heappop(node_pq)
            parent = Node(None, left.count + right.count)
            parent.right = right
            parent.left = left
            left.parent = parent
            right.parent = parent
            heappush(node_pq, (parent.count, parent))

        self.root = node_pq[0]

    def encode(self, message):
        ret = ''
        for char in message:
            status, encoded_char = self.encode_char(char)
            ret += encoded_char
            if not status:
                return "CHAR" + str(char) + "NOT VALID"
        return ret

    def encode_char(self, char):
        curr = None
        e_char = ''
        # The edge case for only one char
        if len(self.leaf_list) == 1 and char == self.root.data:
            return True, '0'
        # General case
        for l in self.leaf_list:
            curr = l if char == l.data else None
        if curr is None:
            return False, "NOT VALID MESSAGE"
        while curr is not self.root:
            e_char += '0' if curr.parent.left is curr else '1'
        return True, e_char

    def decode(self, message):
        curr = self.root
        if self.root.is_leaf():
            return self.root.data
        ret = ''
        for i in message:
            if i == '0':
                curr = curr.left
                if curr.is_leaf():
                    ret += curr.data
                    curr = self.root
            else:
                curr = curr.right
                if curr.is_leaf():
                    ret += curr.data
                    curr = self.root
        return ret


# The following code is copied from GeeksForGeeks
# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)


# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print("%s" % (root.data)),
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)


def height(node):
    """
    Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
    """
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1


if __name__ == '__main__':

    tree = Huffman_Tree('aaabb')
    tree.encode('a')
    # print(decode(root, '0010111101110111100011101110000111000101111100'))