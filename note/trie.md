# Trie

It seems people pronounce it as "try". I was pronouncing "turii", but it's wrong.

## Concept

- Also called `prefix tree`.
  - Because all the descendants of a node have a common prefix string.
- A special form of a `N-ary tree`.
- Used to store strings.
  - Each node in Trie is a string or a prefix
  - The value of a node is the letters from the root to the current node.
- Root is empty string

## Data Structure

- Use `hashmap` to store children nodes.
  - Key is the characters, and value is the child node.
  - A little slower than using the below array
  - But it saves space because it stores only what we need
  - And flexible because it doesn't need to specify a fixed length in advance like an array.
- Use `array` to store children nodes.
  - Fast and easy to visit a node by index.
  - But waste of space because some element might not be used.
- Each Trie node represents a string but may not be meaningful.
  - If we wanna store words in Trie, a node could be in the middle of forming a word
    - e.g. book: b -> bo -> boo -> book. Only book is meaningful, but others are incomplete.
  - We might need to have a `boolean flag` to represent whether current node is a word or not
- There is no convenient built-in data structure tool like `heapq` or `collections.deque` in Python.
  - We have to make Trie data structure by `class` with `collections.defaultdict`.
- [Template: Trie Python code](https://github.com/yukikitayama/leetcode-python/blob/main/algorithm/trie/Trie.py)
- The below is the implementation of Trie without class

```python
import collections

# Instantiate Trie data structure
Trie = lambda: collections.defaultdict(Trie)
trie = Trie()

# Add strings to Trie
words = ['abc', 'def']
for word in words:
    curr = trie
    for c in word:
        curr = curr[c]
    
    # Mark as the end of word
    curr['is_word'] = True
    # or
    # curr[True] = word
```

## Operation

### Insert

- It's the loop starting from the room.
- In each node, it decides
  - Choose a child
  - Or add a new child
- Repeat until it reaches the end
- If it's inserting a word in Trie, the end node represents the word.

### Search Prefix

- For each character in a prefix, loop through Trie
- Search fails if the current character does not exist in Trie
- Search is successful if the loop finds all the characters in going down from the root to children nodes

### Search Word

- Trie needs to have `boolean flag` to represent whether current node is a word.

## Complexity

- Time is `O(N)` because the length of a word to be inserted or searched is `N`, and the operations go down the Trie 
  height `N + 1` from the root to bottom.
  - `+1` because of the first empty root node.
- Space is `O(N * M * K)`
  - `N`: The length of a word
  - `M`: The number of words
  - `K`: The number of characters that each node has
    - `K` is typically 26 for the alphabets and inserting/searching an English word.
  - In the worst case, no words have a common prefix with each other.
  - In practice, space is not such bad, because many words share the same prefix.

## Application

- Autocomplete
- Spell checker

## LeetCode

- [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
  - The most basic problem need to understand
- [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
  - Wild card modification to search operation

## Resource

- LeetCode Explore Card: Trie.
