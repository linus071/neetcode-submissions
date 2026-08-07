# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1,2,3,4,5,6,7] n = 2, [1,2,3,4,5,7]
        # We can do is loop to len_list - n
        dummy = ListNode(0)
        dummy.next = head
        curr_count = dummy
        len_list = 0
        count = 0

        while curr_count:
            len_list += 1
            curr_count = curr_count.next

        curr = dummy
        while count < len_list - n - 1 and curr:
            curr = curr.next
            count += 1
        
        curr.next = curr.next.next
        
        return dummy.next
        