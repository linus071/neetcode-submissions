class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count = 0
        max_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count += 1
                if curr_count > max_count:
                    max_count = curr_count
            else:
                curr_count = 0

        return max_count