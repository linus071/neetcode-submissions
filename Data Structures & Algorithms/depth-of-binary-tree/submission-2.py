from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS: O(N) Time | O(N) Space 
        if not root:
            return 0
            
        q = deque([root])
        lvl = 0

        while q:
            # SNAPSHOT TRICK: range(len(q)) locks in ONLY the nodes currently on this level.
            #For example first round would have [root] appended then look at root left and right child
            #Added in q, then will based on popleft to go through that level then continue the child nodes
            for i in range(len(q)):
                node = q.popleft()
                
                # Append children for the NEXT level (the current 'for' loop ignores them)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Entire level processed
            lvl += 1
        
        return lvl