class TrieNode:
    def __init__(self):
        self.children = {}    # letter -> TrieNode
        self.isWord = False   # True if a word ENDS here

    def addWord(self, word):
        # Standard trie insert, starting from this node (the root)
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Put ALL words in one trie, so a single DFS can
        #    search for every word at the same time
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res = set()    # set so a word found twice is only added once
        visit = set()  # cells on the CURRENT path (can't reuse a cell)

        def dfs(r, c, node, word):
            # Stop if: out of bounds, cell already on this path,
            # or no word in the trie continues with this letter (pruning!)
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or board[r][c] not in node.children):
                return

            visit.add((r, c))                  # choose this cell
            node = node.children[board[r][c]]  # step down the trie
            word += board[r][c]                # The words is in Trie and u add it after u check prev
                                               # is in node.children
            if node.isWord:
                res.add(word)                  # found a full word, keep going
                                               # (a longer word may continue)

            # Explore all 4 neighbours
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r, c))  # backtrack: free the cell for other paths

        # 2. Start a DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)