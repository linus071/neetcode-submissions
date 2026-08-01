class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Doing the Bucket Sort way instead using .sort()
        #Key thing is having that frequency array of size len(nums) + 1, because no matter what won't exceed that
        count = {}
        freq = [[] for i in range (len(nums) + 1)]

        #Now doing count in nums
        #the index is nums and value is count
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #Adding into freq table switching the index is count and value is num
        for n, c in count.items():
            freq[c].append(n)
        
        res=[]
        #since the freq is [0,1,2,3,4...] so doing descending is from highest to lowest
        for i in range (len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        