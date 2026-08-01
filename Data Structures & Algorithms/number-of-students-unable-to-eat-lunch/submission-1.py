class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #Efficient way with Time Complexity of O(n) by using HashSet
        #Going to use Counter is a specialized dictionary subclass from the built-in collections module designed specifically to count the frequency of elements inside an iterable 

        res = len(students)
        count = Counter(students)

        for s in sandwiches:

            if count[s] > 0:
                res -= 1
                count[s] -= 1
            else:
                return res
        
        return 0