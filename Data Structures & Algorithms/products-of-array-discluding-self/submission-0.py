class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Optimal method using Prefix and Postfix
        #But I think left and right is easier to understand
        #Basically run two for loops first is just store the product of left on the curr nums[i]
        #Second loop is just multiply with the product on nums[i] to the right this time

        res = [1] * (len(nums))
        left = 1

        for i in range (len(nums)):
            res[i] = left
            left *= nums[i]
        
        right = 1
        for j in range (len(nums) - 1, -1, -1):
            res[j] *= right
            right *= nums[j]
        
        return res

