# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # ==========================================
        # ALGORITHM: DFS with Boundaries
        # ==========================================
        # TIME: O(N) - We visit every node exactly once.
        # SPACE: O(N) - Recursion stack in the worst-case (a completely unbalanced tree).

        def valid(node, min_val, max_val):
            # Base Case: Empty nodes are technically valid BSTs
            if not node:
                return True
                
            # Boundary Check: Node must be strictly between its floor and ceiling
            if not (min_val < node.val < max_val):
                return False
        
            # Recursive Step: 
            # - Going LEFT updates the CEILING (max_val = node.val)
            # - Going RIGHT updates the FLOOR (min_val = node.val)
            return (valid(node.left, min_val, node.val) and 
                    valid(node.right, node.val, max_val))
            
        # Start at root with no rules (-infinity to +infinity)
        return valid(root, float('-inf'), float('inf'))