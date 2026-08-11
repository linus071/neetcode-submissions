# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # TIME COMPLEXITY: O(N log k) where N is total nodes, k is number of lists.
        # SPACE COMPLEXITY: O(k) for the merged_lists temporary array.
        
        # Edge Case: If the input array is empty, there is nothing to merge.
        if not lists or len(lists) == 0:
            return None
        
        # DIVIDE AND CONQUER
        # We loop until we have condensed all the lists down to exactly 1 final merged list.
        while len(lists) > 1:
            merged_lists = []

            # Step by 2 so we can grab pairs of lists (e.g., list 0 & 1, then list 2 & 3)
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                
                # If there's an odd number of lists, the last one won't have a pair.
                # We safely assign l2 to None if (i + 1) is out of bounds.
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                # Merge the pair and store the result in our temporary array.
                merged_lists.append(self.mergeSort(l1, l2))
            
            # Overwrite the original lists array with our new, half-as-long merged array.
            # This sets us up for the next pass of the while loop.
            lists = merged_lists
            
        # Once the while loop breaks, the only item left at index 0 is our fully merged linked list.
        return lists[0]

    # HELPER FUNCTION: Merges two sorted linked lists (Standard LeetCode #21)
    def mergeSort(self, l1, l2):
        # Dummy node acts as a placeholder to avoid edge cases with the head node.
        dummy = ListNode()
        tail = dummy

        # Traverse both lists as long as NEITHER is empty.
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            # Move the tail pointer forward so we can attach the next node.
            tail = tail.next
            
        # When the while loop finishes, one list might still have leftover nodes.
        # We simply attach the rest of the remaining list to the end of our tail.
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        # Return dummy.next because dummy itself is just the 0-value placeholder.
        return dummy.next