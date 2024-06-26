class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposite = {')' : '(', ']' : '[', '}' : '{'}
        
        for i in s : 
            if len(stack) == 0 : 
                stack.append(i)
            elif opposite.get(i, '') == stack[-1] :
                stack.pop()
            else : 
                stack.append(i)
                
        return len(stack) == 0