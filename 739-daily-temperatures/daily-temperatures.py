class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize a stack to store temperature for a day + it's index
        stack = []
        t = len(temperatures)
        results = [0] * t # default value is 0
        # traverse the temperatures array using index i
        for i in range(t):
            # at each step, while the stack is non empty
            # and top of stack < current element
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # pop top of stack, get it's index j
                j = stack.pop()
                # add the diff i-j to the jth position in the results array
                results[j] = i-j
            # once loop ends, add current element, i 
            stack.append(i)
        return results
