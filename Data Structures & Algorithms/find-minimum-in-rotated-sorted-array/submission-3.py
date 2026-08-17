class Solution:
    def findMin(self, nums: List[int]) -> int:
        # ==========================================
        # ALGORITHM: Modified Binary Search
        # ==========================================
        # TIME COMPLEXITY: O(log N) - Halving the search space each time.
        # SPACE COMPLEXITY: O(1) - Only using pointers.
        
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            # 1. EARLY EXIT (The "Radar" Optimization)
            # If the current window is perfectly sorted (left < right), there is no rotation dip here.
            # The smallest element in a sorted chunk is ALWAYS the first one. Grab it and stop!
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # 2. CHECK MIDDLE
            m = (l + r) // 2
            res = min(res, nums[m]) # Always log the middle value just in case it's the absolute minimum
            
            # 3. CHOOSE WHICH HALF TO SEARCH
            # We are looking for the "dip" (where the rotation happened).
            
            # If the left value is <= mid value, the LEFT portion is perfectly sorted.
            # This means the "dip" hasn't happened yet, so it MUST be in the RIGHT portion.
            if nums[l] <= nums[m]:
                l = m + 1
                
            # If left > mid, the LEFT portion is unsorted.
            # This means the "dip" MUST be trapped somewhere in the LEFT portion.
            else:
                r = m - 1

        return res