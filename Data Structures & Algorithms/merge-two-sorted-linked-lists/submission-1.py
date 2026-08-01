# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Recursion method
        #Example: list1: [1] -> [4] -> None
        #         list2: [2] -> [3] -> None
        # To find out who stands behind it, it takes the rest of its own list (list1.next, which is Node 4) and the entire other list (list2, which is Node 2 and 3), and throws them back into the function to let them battle it out.
        # Plaintext
        # [ Node 1 ] -> .next = self.mergeTwoLists([4], [2, 3])

        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
