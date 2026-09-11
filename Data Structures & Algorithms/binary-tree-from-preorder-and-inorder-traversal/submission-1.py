# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # ==========================================
        # ALGORITHM: HashMap + Pointers
        # ==========================================
        # TIME: O(N) - We visit each node once, and dictionary lookup is O(1).
        # SPACE: O(N) - For the dictionary and the recursion stack.

        # 1. Map values to their inorder indexes for instant O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 2. Track our current "Boss" in the preorder array
        preorder_idx = 0

        # 3. Helper function uses indices (left, right) instead of slicing arrays
        def build(left, right):
            nonlocal preorder_idx # Allows us to modify the counter from the outer function
            
            # Base Case: If the boundaries cross, there are no nodes for this subtree
            if left > right:
                return None
            
            # Identify the boss and create the node
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            preorder_idx += 1 # Move the pointer to the next boss
            
            # Find where this boss splits the inorder array
            mid = inorder_map[root_val]
            
            # Recursively build the left and right teams
            # Left team is bounded from 'left' to 'mid - 1'
            root.left = build(left, mid - 1)
            # Right team is bounded from 'mid + 1' to 'right'
            root.right = build(mid + 1, right)
            
            return root
            
        # Start the recursion with boundaries covering the entire inorder array
        return build(0, len(inorder) - 1)