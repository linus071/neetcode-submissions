from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ==========================================
        # KEY CONCEPT: The "Have vs. Need" Pattern
        # ==========================================
        # 1. 'need' = Total number of UNIQUE characters in 't'.
        # 2. 'have' = How many unique characters in our window meet the required frequency.
        # 3. EXPAND (move r) until have == need.
        # 4. SHRINK (move l) while have == need to find the minimum length.
        # 
        # TIME: O(N + M) - We iterate through s and t once.
        # SPACE: O(1) - Dictionaries hold at most 52 English letters.

        l = 0
        best_l, best_r = 0, 0
        min_len = float('inf')
        
        t_set = Counter(t) 
        have, need = 0, len(t_set) 
        
        map_string = {} # Tracks frequencies of ONLY the target chars in our window

        for r in range(len(s)):
            
            # --- PHASE 1: EXPAND THE WINDOW ---
            # OPTIMIZATION: Ignore useless characters. Only add to map_string if it's in t_set.
            if s[r] in t_set:
                map_string[s[r]] = 1 + map_string.get(s[r], 0)
                
                # If our window's count EXACTLY MATCHES the target count, we satisfied one unique char
                if t_set[s[r]] == map_string[s[r]]:
                    have += 1

            # --- PHASE 2: SHRINK THE WINDOW ---
            # As long as our window is valid, try to make it smaller
            while have == need:
                
                # 1. Record the new minimum window
                if min_len > r - l + 1:
                    # OPTIMIZATION: Save indices instead of the whole string to save massive amounts of memory
                    min_len = r - l + 1
                    best_l, best_r = l, r
                
                # 2. Try removing the left-most character
                if s[l] in t_set:
                    map_string[s[l]] -= 1
                    
                    # If removing it drops the count STRICTLY BELOW what we need, the window becomes invalid
                    if t_set[s[l]] > map_string[s[l]]:
                        have -= 1
                        
                # 3. Actually slide the left pointer
                l += 1

        # Return the sliced string using our saved indices. If min_len is still infinity, we found nothing.
        return s[best_l: best_r + 1] if min_len != float('inf') else ""