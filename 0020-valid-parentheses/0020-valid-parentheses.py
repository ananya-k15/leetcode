class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 : 
            return False
        stack = []
        pair = {')' : '(', '}' : '{', ']' : '['}
        for i in s :
            if i in pair.keys() and len(stack) >= 1 and stack[-1] == pair[i] : 
                    stack.pop()
            else : 
                stack.append(i)
        if not stack : 
            return True
        return False    