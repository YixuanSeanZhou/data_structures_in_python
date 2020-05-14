from typing import List


class Node:
    """
    Nodes in the trie
    """

    def __init__(self):
        """
        Constructor of the node.
        """
        self.word_node = False
        self.out_going_paths = {}

    def __repr__(self):
        return "Is word node: " + str(self.word_node) + '\n' +\
            "Out going paths: " + str(list(self.out_going_paths.keys()))

    def set_to_word_node(self):
        self.word_node = True

    def unset_word_node(self):
        self.word_node = False

    def add_path(self, char: str, end: bool) -> bool:
        if self.out_going_paths.get(char):
            # duplicate
            return False
        child = Node()
        if end:
            child.set_to_word_node()
        self.out_going_paths[char] = child
        sort_path = {}
        for key in sorted(self.out_going_paths):
            sort_path[key] = self.out_going_paths[key]
        self.out_going_paths = sort_path
        return True

    def remove_path(self, char: str) -> bool:
        if char in self.out_going_paths:
            del self.out_going_paths[char]
            return True
        else:
            return False

    def auto_complete(self) -> List[str]:
        """
        Find a list of words that ended with a node.
        """
        return self.accend_order_traversal('')

    def accend_order_traversal(self, curr_str: str) -> List[str]:
        s_list = []
        if self.word_node:
            s_list.append(curr_str)
        for key in self.out_going_paths.keys():
            # add the key in the list and recurse down
            tmp = curr_str + key
            s_list += self.out_going_paths[key].accend_order_traversal(tmp)
        return s_list


class Trie:
    """
    The Trie class
    """
    def __init__(self):
        """
        Init an empty Trie
        """
        self.root = Node()
        self.num_node = 1

    def find(self, word: str) -> (Node, bool, bool):
        """
        Return the Node that ended the search (if there is one).
        The first bool represents whether we have the item in the Trie.
        The second bool indecate whether it is a completed word
        """
        char_list = list(word)
        index = 0
        curr_node = self.root
        while index < len(char_list):
            if char_list[index] in curr_node.out_going_paths:
                curr_node = curr_node.out_going_paths[char_list[index]]
                if index == len(char_list) - 1 and curr_node.word_node:
                    print(curr_node.word_node)
                    return curr_node, True, True
            else:
                return None, False, False
            index += 1
        return curr_node, True, False

    def insert(self, word: str) -> bool:
        char_list = list(word)
        index = 0
        curr_node = self.root
        while index < len(char_list):
            if char_list[index] in curr_node.out_going_paths:
                curr_node = curr_node.out_going_paths[char_list[index]]
                end = index == len(char_list) - 1
                if end:
                    curr_node.set_to_word_node()
                index += 1
            else:
                end = index == len(char_list) - 1
                curr_node.add_path(char_list[index], end)
                self.num_node += 1

    def remove(self, word: str) -> bool:
        char_list = list(word)
        index = 0
        curr_node = self.root
        while index < len(char_list):
            if char_list[index] in curr_node.out_going_paths:
                curr_node = curr_node.out_going_paths[char_list[index]]
                if index == len(char_list) - 1 and curr_node.word_node:
                    curr_node.unset_word_node()
                    return True
            else:
                return False
            index += 1
        return False


if __name__ == '__main__':
    Trie = Trie()
    Trie.insert('TheFastAndTheFurious')
    Trie.insert('2Fast2Furious')
    Trie.insert('TheFastAndTheFuriousTokyoDrift')
    Trie.insert('FastAndFurious')
    Trie.insert('FastFive')
    Trie.insert('FastAndFurious6')
    Trie.insert('Furious7')
    Trie.insert('TheFateOfTheFurious')
    Trie.insert('FastAndFuriousPresentsHobbsAndShaw')
    Trie.insert('F9')
    print(Trie.num_node)
