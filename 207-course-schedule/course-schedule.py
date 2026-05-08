class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courseMap = {x:[] for x in range(0, numCourses)}
        for c, prereq in prerequisites:
            courseMap[c].append(prereq)

        courses = [x for x in range(numCourses)]
        safe = set()
        visiting = set()
        
        def explore(course):
            if course in safe:
                return True
            visiting.add(course)
            for prereq in courseMap[course]:
                if prereq in visiting or explore(prereq) == False:
                    return False
            visiting.remove(course)
            return True

        for c in courses:
            if explore(c):
                safe.add(c)
            else:
                return False

        return True

            

        
         