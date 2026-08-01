class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Do Reverse order and last element would be -1
        #Compare the curr max and element on right as we reversing
        rightMax = -1
        replace_arr = arr

        for i in range(len(arr)-1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax

        return arr
