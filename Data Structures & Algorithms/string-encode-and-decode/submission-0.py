class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            encoded_string = str(len(word)) + "$"
            res.append(encoded_string + word)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        end = 0
        
        while start < len(s):
           
            while s[end] != "$":
                end += 1
            len_word = int(s[start:end])
            start = end + 1
            end = start + len_word
            res.append(s[start:end])
            start = end
        
        return res
