class Solution:
    def isValid(self, s: str) -> bool:
        closing_set = {"}":"{", ")":"(", "]":"["}
        res = []

        for char in s:
            print(res)
            if res and char in closing_set:
                if res[-1] == closing_set[char]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)
        
        return True if not res else False
            




