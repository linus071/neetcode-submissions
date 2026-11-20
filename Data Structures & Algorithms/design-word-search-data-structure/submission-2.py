class TrieNode:
    def __init__(self):
        self.children = {}   # letter -> TrieNode
        self.word = False    # True if a word ENDS at this node (not just a prefix)

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()   # empty root, holds no letter

    def addWord(self, word: str) -> None:
        # Standard trie insert: walk down, creating nodes as needed
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True   # mark the last node as a complete word

    def search(self, word: str) -> bool:
        # dfs(j, root): can word[j:] be matched starting from node `root`?
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    # Wildcard: try EVERY child as the match for this letter,
                    # then keep matching the rest (word[i+1:]) from that child
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True   # one path worked, stop early
                    return False          # no child led to a match

                else:
                    # Normal letter: follow it like a regular trie search
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            # Used up all letters: only a match if a word ends here
            return curr.word

        return dfs(0, self.root)

# Time: addWord O(n). search O(n) without dots; with up to 2 dots
#       it's O(26^2 * n), which is still O(n).
# Space: O(t + n), where t = total trie nodes and n = recursion depth.
# Key lessons:
#   1. Always mark end-of-word. Reaching the end of the input isn't enough.
#   2. The '.' branch returns inside the loop, because the recursive call
#      already handled the rest of the word.