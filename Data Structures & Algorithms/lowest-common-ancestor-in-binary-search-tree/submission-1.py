# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #Can do DFS recursive to find the common ancestor node of p and q 
        #Left subtree is lesser and right subtree is greater than the node. We can do if when traverse to a different subtree to left or right we return that node 
        print(root.val)
        if not root:
            return None

        
        if (root.val <= p.val and root.val >= q.val) or (root.val >= p.val and root.val <= q.val):
            return root
        elif root.val > p.val and root.val > q.val:
            print("here")
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        
