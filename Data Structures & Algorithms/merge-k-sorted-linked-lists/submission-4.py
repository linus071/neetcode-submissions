# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Instead doing just simple merge sort one by one
        #Will do Divide and Conquer, which is merge sort 2 by 2 which is faster
        if not lists:
            return None
        
        while len(lists) > 1:
            merged_lists = []

            for i in range (0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                merged_lists.append(self.mergeSort(l1,l2))
            lists = merged_lists
        return lists[0]

    def mergeSort(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        return dummy.next







