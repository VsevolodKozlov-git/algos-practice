from typing import List
class Solution:
    def findOrder(self, numCourses: int, inp_shit: List[List[int]]) -> List[int]:
        course_req = [[] for i in range(numCourses)]
        for course, requirement in inp_shit:
            course_req[course].append(requirement)

        ordered_courses = []
        while True:
            if len(ordered_courses) == numCourses:
                break
            for course_req in
            # find max prerequirements
            # itera-req find all requirements

if __name__ == '__main__':
    Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])