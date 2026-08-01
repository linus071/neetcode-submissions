class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # --- ALGORITHM BLUEPRINT ---
        # 1. Sort the array first to enable the Two-Pointer technique.
        # 2. Iterate through with 'a'. The remaining two numbers must equal (0 - a).
        # 3. Use left (l) and right (r) pointers to find those remaining two numbers:
        #    - If sum < 0: We need a bigger number (increment l)
        #    - If sum > 0: We need a smaller number (decrement r)
        # 4. To avoid duplicate triplets, skip adjacent duplicate numbers for both 'a' and 'l'.
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            # Skip duplicate 'a' values to prevent duplicate triplets in the result.
            # (i > 0 ensures we don't go out of bounds checking the previous element)
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    # Found a valid triplet!
                    res.append([a, nums[l], nums[r]])
                    
                    # Move the left pointer forward to search for new combinations.
                    l += 1
                    
                    # Skip duplicate 'l' values to avoid logging the exact same triplet again.
                    # Note: We only need to manually shift 'l'. If we shift 'l' to a larger number, 
                    # the next loop's 'threeSum' will be > 0, naturally forcing 'r' to decrement.
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        
        return res