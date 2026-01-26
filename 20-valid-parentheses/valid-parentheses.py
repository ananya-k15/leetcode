class Solution:
    def isValid(self, s: str) -> bool:
        # start an empty stack
        stack = []
        matching = {'}':'{', ']':'[', ')':'('}

        # for each letter x in s
        for x in s:
            # if x is a starting parenthesis, 
            if x in '([{':
                # add it to the stack
                stack.append(x)
            # otherwise, check whether the last letter matches the closing parentheses
            elif len(stack) > 0 and matching.get(x, "") == stack[-1]:
                # if so, pop the last letter 
                stack.pop()
            # if not, return invalid
            else:
                return False

        # if the loop ends successfully and the stack is empty
        if stack == [] :
            # return valid
            return True
        
        # otherwise invalid
        return False