class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Input [1, 1, 2, 2, 2, 3, 3, 3, 4] k = 2
        #Output [2, 3]
        #We can do HashTable counter to find frequency of each number
        #Creat a hashtable, do counter. Then create an array switch their position when adding in and sort
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
  
        return res