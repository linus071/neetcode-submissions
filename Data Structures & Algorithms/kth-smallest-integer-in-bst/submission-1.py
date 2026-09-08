# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        count = 0
        curr = root

        # CONDITION GOTCHA: Must be `curr OR stack`. 
        # If stack is empty but curr just moved to a right child, we still need to process it.
        while curr or stack:
            
            # 1. THE PLUNGE
            # Dive as deep left as possible. Leftmost = smallest.
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # 2. THE GOTCHA MOMENT: Popping == Visiting in sorted order!
            # The instant you pop from the stack is the instant you are reading 
            # the tree in perfectly sorted, ascending order.
            curr = stack.pop()
            count += 1
            
            # 3. EARLY EXIT
            if count == k:
                return curr.val
                
            # 4. THE PIVOT
            # We finished the left and the node itself. Now explore the right.
            # GOTCHA: Do NOT append right to the stack here. 
            # Just point `curr` to it and let the loop plunge left again.
            curr = curr.right

        return -1