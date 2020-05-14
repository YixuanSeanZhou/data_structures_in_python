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


class Huffman_Tree:

    def __init__(self, s_to_encode):
        c_count = {}
        for char in s_to_encode:
            if char in c_count:
                c_count[char] += 1
            else:
                c_count[char] = 0
        char_count_list = [(k, v) for k, v in dict.items()]
        self.root, self.leaves = self.build_tree(char_count_list)

    def build_tree(char_count_list):
        node_pq = []
        for pair in char_count_list:
            node = Node(pair[0], pair[1])
            heappush(node_pq, (node.count, node))
        leaf_list = []

        for node in node_pq:
            leaf_list.append(node)

        while len(node_pq) > 1:
            _, left = heappop(node_pq)
            _, right = heappop(node_pq)
            parent = Node(None, left.count + right.count)
            parent.right = right
            parent.left = left
            left.parent = parent
            right.parent = parent
            heappush(node_pq, (parent.count, parent))

        root = node_pq[0]
        return root, leaf_list

    def encode(self, message):
        ret = ''
        for char in message:
            status, encoded_char = self.encode_char(char)
            ret += encoded_char
            if not status:
                return "CHAR" + str(char) + "NOT VALID"

    def encode_char(self, char):
        curr = None
        e_char = ''
        for l in self.leaves:
            curr = l if char == l.data else None
        if curr is None:
            return False, "NOT VALID MESSAGE"
        while curr is not self.root:
            e_char += '0' if curr.parent.left is curr else '1'
        return True, e_char

    def decode(self, message):
        curr = self.root
        if root.is_leaf():
            return root.data
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
    char_count_list = [('+', 16), ('O', 23), ('A', 30), ('C', 40), ('E', 41), ('S', 44), ('N', 52), ('R', 68), ('T', 75), ('H', 82), ('I', 87)]
    root = build_tree(char_count_list)
    printLevelOrder(root)
    print(decode(root, '0010111101110111100011101110000111000101111100'))