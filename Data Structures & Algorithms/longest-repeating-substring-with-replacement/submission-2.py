class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ALGORITHM: Sliding Window (Optimized)
        # TIME COMPLEXITY: O(N) - We iterate through the string exactly once.
        # SPACE COMPLEXITY: O(1) - The dictionary holds at most 26 uppercase English letters.
        
        # CORE LOGIC: A window is valid if: (Window Length) - (Max Char Frequency) <= k
        # This means the number of "other" characters we need to replace is within our limit 'k'.

        count = {}
        res = 0
        l = 0
        maxf = 0 # Tracks the historically highest frequency of a single char in our window

        for r in range(len(s)):
            # 1. EXPAND THE WINDOW
            # Add the new character at the right pointer to our count map
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # 2. UPDATE HISTORICAL MAX FREQUENCY
            # TRICKY PART: We only ever increase maxf. When 'l' moves and a character's count drops, 
            # we DO NOT decrement maxf. Why? Because we only care about finding a LONGER valid window. 
            # A longer window is only mathematically possible if we find a new maxf that beats our old one.
            maxf = max(maxf, count[s[r]])

            # 3. IF INVALID, SLIDE THE WINDOW (DON'T SHRINK)
            # If characters to replace > k, the window is invalid.
            # By using 'if' instead of 'while', we slide the window across the string at its current 
            # maximum size, rather than shrinking it down.
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            # 4. RECORD THE MAX LENGTH
            res = max(res, r - l + 1)
                
        return res