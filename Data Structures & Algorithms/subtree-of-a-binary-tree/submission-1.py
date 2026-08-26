# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Use the same concept of the same tree
        #Need to find the first node of subroot first in root, can use BFS to do it
        q = deque([root])

        if not root:
            return False
        if not subRoot:
            return True

        while q:
            for i in range (len(q)):
                node = q.popleft()

                if node.val == subRoot.val and self.sameTree(node, subRoot) :
                    return True
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return False


    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        
        else:
            return False