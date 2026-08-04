# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # --- ALGORITHM BLUEPRINT ---
        # 1. Split list in half: Use slow/fast pointers. 
        #    (fast starts at head.next to ensure we get the left-middle on even lists).
        # 2. Reverse the second half: Standard linked list reversal.
        # 3. Alternate merge: Zip list 1 and list 2 together like a zipper.
        
        # ==========================================
        # STEP 1: Find the middle and cut the cord
        # ==========================================
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 'slow' is now the end of the first half. 
        # 'l2' becomes the start of the second half.
        l2 = slow.next
        
        # Cut the connection so the first half doesn't loop into the second!
        slow.next = None 

        # ==========================================
        # STEP 2: Reverse the second half (l2)
        # ==========================================
        curr, prev = l2, None
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
            
        # ==========================================
        # STEP 3: Alternate merge l1 and l2
        # ==========================================
        # l1 is the head of the first half. 'prev' is the new head of the reversed second half.
        l1, l2 = head, prev
        
        # print(l1.val, l2.val)  <-- Good for debugging!
        
        while l2:
            # Example: l1 = [1,2], l2 = [5,4,3]
            # Save the next nodes before we overwrite the pointers
            temp_l1, temp_l2 = l1.next, l2.next
            
            # Zip them together: l1 points to l2, l2 points to the rest of l1
            l1.next, l2.next = l2, temp_l1
            
            # Shift our main pointers forward to the saved nodes for the next loop
            l1, l2 = temp_l1, temp_l2