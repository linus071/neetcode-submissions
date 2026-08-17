class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #High level
        #Need to find m first
        #Then see if is left portion or right portion

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            #left portion
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            
                
            #right portion
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1