class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ALGORITHM: Sliding Window
        # TIME COMPLEXITY: O(N) - Each character is visited at most twice (once by r, once by l).
        # SPACE COMPLEXITY: O(1) - The set will hold at most the number of characters in the alphabet (e.g., 128 ASCII chars).
        
        longestcset = set() # Tracks the unique characters currently inside our window
        max_count = 0       # Stores the maximum window size we've seen so far
        l, r = 0, 0         # Left and Right pointers that define the edges of our window

        while r < len(s):
            # EXPAND THE WINDOW: 
            # If the character is not in our set, it's safe to add.
            if s[r] not in longestcset:
                longestcset.add(s[r])
                # Calculate the window size BEFORE incrementing r
                max_count = max(max_count, r - l + 1)
                r += 1 
                
            # SHRINK THE WINDOW:
            # If we hit a duplicate, we must shrink from the left side until the duplicate is gone.
            else:
                longestcset.remove(s[l])
                l += 1
                
                # Note: We DO NOT increment 'r' here! 
                # The loop restarts, and the 'if' statement will check this exact same s[r] 
                # again until the duplicate has been completely removed by 'l'.
                
        return max_count