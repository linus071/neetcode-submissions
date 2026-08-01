class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_cons = 0

        for num in hash_set:
            # ONLY start counting if 'num' is the very first number in a sequence.
            # If (num - 1) exists, 'num' is in the middle of a chain, so we skip it to save time!
            if (num - 1) not in hash_set:
                count = 1  # We found a starting line. Sequence length is currently 1 (just this number).
                
                # Keep checking if the next consecutive numbers exist to build the chain
                while (num + count) in hash_set:
                    count += 1
                
                # Update the longest sequence found so far
                max_cons = max(count, max_cons)

        return max_cons