class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize a stack to store temperature for a day + it's index
        stack = []
        t = len(temperatures)
        results = [0] * t # default value is 0
        # traverse the temperatures array using index i
        for i in range(t):
            current = temperatures[i]
            # at each step, while the stack is non empty
            # and top of stack < current element
            while stack != [] and stack[-1][0] < current:
                # pop top of stack, get it's index j
                j = stack[-1][1]
                stack.pop()
                # add the diff i-j to the jth position in the results array
                results[j] = i-j
            # once loop ends, add current element, i 
            stack.append([current, i])
        return results
