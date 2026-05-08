class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # create adjacency list
        courseMap = {x: [] for x in range(numCourses)}
        inDegree = [0 for x in range(numCourses)]
        for c, prereq in prerequisites:
            courseMap[prereq].append(c)
            inDegree[c] += 1

        # pick out all courses with no dependencies
        source = deque([])
        for ind in range(numCourses):
            if inDegree[ind] == 0:
                source.append(ind)
        if source == []:
            return [] # there is a cycle

        order = []
        # there are the source nodes we initiate the queue with 
        while len(source) != 0:
            # at each "level", for the number of courses in the level
            course = source.pop()
            order.append(course)
            for prereq in courseMap[course]:
                inDegree[prereq] -= 1
                if inDegree[prereq] == 0:
                    source.append(prereq)
    
        if len(order) != numCourses:
            return []
        return order

