class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    '''
    Approach:
    1. Use TrieNode
    2. For __init__ - initialize the Tries data structure
    3. For addWord - add each word to the Tries data structure
    4. For seach:
       - need to handle "." that can be matched with any letter
    '''
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Use DFS to search for each branch
        def dfs(index, node):
            cur = node

            # Traverse each branch until it match
            for i in range(index, len(word)):
                c = word[i]
                # Handles "."
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                # Handles char
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        
        # Execute DFS from root
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
