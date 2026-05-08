class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courseMap = {x:[] for x in range(0, numCourses)}
        for c, prereq in prerequisites:
            courseMap[c].append(prereq)

        safe = set()
        visiting = set()
        
        def explore(course):
            if course in safe:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for prereq in courseMap[course]:
                if not explore(prereq):
                    return False
            visiting.remove(course)
            safe.add(course)
            return True

        return all(explore(c) for c in range(numCourses))

            

        
         