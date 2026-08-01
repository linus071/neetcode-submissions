class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #Can have a count, where if count is >= to the len(students) return count (no.of students unable to eat)
        #Count would reset if students took a sandwich
        #Have while loop, conditions: while students and sandwiches
        #if statement inside, if count is >= to the len(students) return count
        #if students[0] == sandwiches [0]: 
        # students.popleft(), sandwiches.popleft()
        # count = 0
        #else:
        # unmatch_student = students[0]
        # students.popleft()
        # students.append(unmatch_student)
        #count += 1
        students_deque = deque(students)
        sandwiches_deque = deque (sandwiches)
        count = 0

        while students_deque and sandwiches_deque:
            if count >= len(students_deque):
                return count
            
            if students_deque[0] == sandwiches_deque [0]:
                students_deque.popleft()
                sandwiches_deque.popleft()
                count = 0
            else:
                unmatch_student = students_deque[0]
                students_deque.popleft()
                students_deque.append(unmatch_student)
                count += 1
        return 0