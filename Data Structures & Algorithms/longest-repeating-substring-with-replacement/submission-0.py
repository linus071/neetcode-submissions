class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Count what char is the most freq for each sliding window basically
        #have left and right pointer as well, if the sliding window length - max_freq of that window is smaller equal to k, the res would be the sliding window length
        count= {}
        res = 0
        l = 0


        for r in range (len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            if r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
                
        
        return res