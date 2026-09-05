# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Instant BFS, go layer by layer then add each one to a list
        res = []
        if not root:
            return res

        q = deque([root])

        while q:
            sublist = []
            for i in range (len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sublist.append(node.val)
            res.append(sublist)
        
        return res