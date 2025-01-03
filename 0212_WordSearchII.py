class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Construct the tries for each words
        root = TrieNode()
        for w in words:
            root.addWord(w)

        # Construct DFS to traverse for each cells
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            # Base
            if (
                r < 0 or c < 0 or r == ROWS or c == COLS or # boundary
                (r, c) in visit or                          # visited
                board[r][c] not in node.children            # not exist in tries
            ):
                return
            
            # Mark cell visited
            visit.add((r, c))
            node = node.children[board[r][c]]

            # Concatenate the word
            word += board[r][c]

            # Check whether word is found
            if node.word is True:
                res.add(word)
            
            # Continue to DFS
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)    
