class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestcset = set()
        max_count = 0
        l, r = 0, 0

        while r < len(s):

            if s[r] not in longestcset:
                #print("not in set", c)
                longestcset.add(s[r])
                max_count = max(max_count, r - l + 1)
                r += 1
            else:
                #print("in set", c)
                longestcset.remove(s[l])
                l += 1
            #print(longestcset)
        return max_count