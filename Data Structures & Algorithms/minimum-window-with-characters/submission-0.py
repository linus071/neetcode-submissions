class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Brain Storm Process:
        # Have two pointers l and r
        # find l index: 1. Loop from i = 0 to any char from t in s first, then removed the char from t
        # find r index: 2. Loop from i = len(s) to any char from t in s second, then removed char from t
        # res = substring based on l and r
        # Check if all of t is in res
        # if not return "", if yes return res
        #Brain Storm process doesn't work
        #Retry instead using two  pointers again but this time will start both from 0 then try to find the substring that contains all in t_set, once found would move left pointer until it doesn't contain all char from t_set then continue pointer r. Already save the res from the previous and just keep comparing then return result. This thinking still very high level.

        l = 0
        best_l, best_r = 0, 0
        map_string = {}
        t_set = Counter(t)
        have, need = 0, len(t_set)
        min_len = float('inf')

        for r in range (len(s)):
            
            if s[r] in t_set:
                map_string[s[r]] = 1 + map_string.get(s[r], 0)
                if t_set[s[r]] == map_string[s[r]]:
                    have += 1

            while have == need:
                if min_len > r - l + 1:
                    #Save index instead the whole string
                    min_len = r - l + 1
                    best_l, best_r = l, r
                
                if s[l] in t_set:
                    map_string[s[l]] -= 1
                    if t_set[s[l]] > map_string[s[l]]:
                        have -= 1
                l += 1

        return s[best_l: best_r + 1] if min_len != float('inf') else ""




