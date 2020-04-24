# Implements Several Advanced Data Structues Via Python

While taking the advanced data structures class (CSE 100) at UCSD, I feel like I should try impelemnt all those in python (maybe for future uses)

### Data Structures Learned

#### Trees:
- Regular BST
  - The worst case time complexity is O(n) (can resulted in a linked list), the average case is O(log(n)) -- given the assumption that the inseration and search order are random.
- Heap (Usually implemented through an array (to access the next insertion point) with parent be (round up)n/2, left child 2n + 1, right child 2n+2
  - Ordered by importance
    - Can very fast peek the most important object (O(1))
  - O(n) for search. 
  - O(log(n)) for insert
  - O(log(n)) for remove
- K-D Tree
  - Deal with storing data in multi-dim
  - Can be useful when tring to find nearest neighbors around a point.
- Treap
  - The is randomnized BST, using both BST and Heap to achieve the randomnized assumptios in the proof of the average case of BST.
  - It can be useful for security reason (no history of the order of insertion) 
- AVL Tree
  - Using AVL rotations to maintain the BST property. Have a balance factor to ensure the tree is balanced
  - Insert O(log(n))
  - Remove O(log(n))
  - Search O(log(n))
- Red-Black Tree
  - Using black-red properties to ensure the tree's balance
  - Insert O(log(n))
  - Remove O(log(n))
  - Search O(log(n))
- Comparing teh AVL Tree and Red-Black Tree:
  - Tree height:
    - Black-red tree can have twice height as AVL tree
  - Time complexity:
    - Given the same height of trees
      - AVL Tree requires to go down the tree to insert, then go up the tree to check the balance.
      - Red-Black tree can insert with only one way down.
  - Thus, if we need more insert and remove comparing to find, Red-Black tree is better. On the other hand, find being mainly used will result in AVL tree having more advantages.
- MutiwayTries
  - Inefficient in space if we pre-determine all the possible ways i.e. the alphabet.
    - Better performance in a dense lexicon.
  - Without pre-determine the alphabet, the algorithm is O(log(n) * k) where k is the size of the alphabet, n is the number of nodes being inserted.
- Ternary Tree
  - Both space and time complexit in between BST and Tries

#### Hash Table
There are three main considerations for a good hash table
1. Hash function
2. Collision resolution
3. Size of the hash table


#### Implemented Data Structues
- Tries (Multiway Trie)
