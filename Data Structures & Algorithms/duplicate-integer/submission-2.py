class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        mySet = set()

        for i in range(len(nums)):
            mySet.add(nums[i])
        
        if len(mySet) == len(nums):
            return False
        
        return True