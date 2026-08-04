# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # --- ALGORITHM BLUEPRINT ---
        # 1. Use Floyd's Tortoise and Hare algorithm (Two Pointers).
        # 2. 'slow' moves 1 step at a time, 'fast' moves 2 steps.
        # 3. If the linked list has a cycle (like a circular running track), 
        #    the 'fast' runner will eventually lap the 'slow' runner and they will meet.
        # 4. If 'fast' hits a dead end (None), there is no cycle.
        slow, fast = head, head

        # We must check fast AND fast.next to prevent errors. 
        # Since fast jumps 2 steps, trying to read fast.next.next when fast.next is None will crash.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # The fast pointer successfully lapped the slow pointer!
            if slow == fast:
                return True

        return False 
