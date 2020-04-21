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
        return True
    
    def remove_path(self, char: str) -> bool:
        if char in self.out_going_paths:
            del self.out_going_paths[char]
            return True
        else:
            return False

class Trie:
    """
    The Trie class
    """
    def __init__(self):
        """
        Init an empty Trie
        """
        self.root = Node()
    
    def find(self, word: str) -> bool:
        char_list = list(word)
        index = 0
        curr_node = self.root
        while index < len(char_list):
            if char_list[index] in curr_node.out_going_paths:
                curr_node = curr_node.out_going_paths[char_list[index]]
                if index == len(char_list) - 1 and curr_node.word_node:
                    print(curr_node.word_node)
                    return True
            else:
                return False
            index += 1
        return False
    
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
    Trie.insert('abc')
    print(Trie.find('abc'))
    print(Trie.find('asdf'))
    Trie.insert('asdf')
    print(Trie.find('asdf'))
    print()
    print('Perform remove')
    print(Trie.remove('asdf'))
    print(Trie.find('asdf'))
    Trie.insert('asdf')
    print(Trie.find('asdf'))
