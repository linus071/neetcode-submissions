class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list) creates a dictionary where any missing key automatically starts with an empty list ([])
        res = defaultdict(list)

        for s in strs:
            #every new word reset count to see, 26 lower capital letters track
            count = [0]*26
            for c in s:
                #every character in each string
                #ord('a') - ord('a')  97 - 97 = 0 (Index 0) ord('c') - ord('a')  99 - 97 = 2 (Index 2)
                count[ord(c) - ord('a')] += 1
            #find existing key and match their count, then append the word into it Example: (1, 0, 1, 0, ...): ["cat", "act"]
            res[tuple(count)].append(s)
            
        return list(res.values())