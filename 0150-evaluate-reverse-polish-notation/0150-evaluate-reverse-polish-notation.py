class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens : 
            if i == '+' : 
                stack.append(stack.pop() + stack.pop())
            elif i == '-' : 
                stack.append(-1 * (stack.pop() - stack.pop()))
            elif i == "*" :
                stack.append(stack.pop() * stack.pop())
            elif i == "/" :
                denom = stack.pop(); nom = stack.pop()
                stack.append(int(nom/denom))
            else :
                stack.append(int(i))
        return int(stack[0])        