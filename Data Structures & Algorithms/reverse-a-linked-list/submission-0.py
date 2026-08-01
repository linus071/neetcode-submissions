# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Recursive way, Example: (1,2,3)

        #Base Case
        if not head:
            return None

        #Would keep assign newHead as it goes down, but 3 would be the newHead as it wont get change after since recursion function is below
        newHead = head
        if head.next:
            #head would get assign as recursive func is called so 1 would be head and 2 would be head once func call
            newHead = self.reverseList(head.next)
            # use 2,3 as exp: 2 (head.next.next) would be 2 pointing 3 and 3 next pointer would be 2, so technically just pointing itself back
            head.next.next = head
        #Need to remove original pointer like [ 2(head) <-> 3(newHead) ] to [ None <- 2 <- 3 ]
        head.next = None

        #Would always return Node3 Linked List as newHead
        return newHead


