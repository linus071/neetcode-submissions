class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = nums
        ans.extend(nums)
        print(ans)
        return ans
