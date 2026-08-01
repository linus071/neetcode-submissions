class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hash_set = set(nums)
        max_cons = 0

        for num in hash_set:
            if (num - 1) not in hash_set:
                count = 1
                while (num + count) in hash_set:
                    count += 1
                max_cons = max(count, max_cons)

        return max_cons
