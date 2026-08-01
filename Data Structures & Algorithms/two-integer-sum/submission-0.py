class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #instead doing a + b = target, can do Hashmap[a] = target - b, so it would be running list just once
        Hash = {}
        for i, b in enumerate(nums):
            a = target - b

            if a in Hash:
                return [Hash[a], i]
            #The reason we store Hash[b] = i is because the hash map acts as your "Seen It" Diary.
            Hash[b] = i
        
        return result