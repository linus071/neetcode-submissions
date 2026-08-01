class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        final_arr = []
        max = 0

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):

                if arr[j] > max:
                    max = arr[j]

            final_arr.append(max)
            max = 0
        
        final_arr.append(-1)
        
        return final_arr
        