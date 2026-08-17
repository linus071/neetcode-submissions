class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # ==========================================
        # KEY CONCEPT: Find the "Perfectly Sorted Zone"
        # ==========================================
        # 1. One half of the array will always be perfectly sorted.
        # 2. Check if the target fits mathematically inside that sorted half.
        # 3. If it doesn't, search the other half.
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m

            # --- LEFT PORTION IS THE PERFECTLY SORTED ZONE ---
            if nums[l] <= nums[m]:
                
                # Check if target is OUTSIDE this sorted zone
                # (Too small for the left edge, or too big for the right edge)
                if target < nums[l] or target > nums[m]:
                    l = m + 1 # Search the right half
                else:
                    r = m - 1 # Target is safely inside, search left half
                    
            # --- RIGHT PORTION IS THE PERFECTLY SORTED ZONE ---
            else:
                
                # Check if target is OUTSIDE this sorted zone
                # (Too big for the right edge, or too small for the left edge)
                if target > nums[r] or target < nums[m]:
                    r = m - 1 # Search the left half
                else:
                    l = m + 1 # Target is safely inside, search right half
        
        return -1