class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create a stack to store intermediate results
        intermediate = []
        # parse the tokens list from left to right 
        for x in tokens:
            # if it's an operator, pop the last two elements from the stack
            if x in "/+-*":
                num2 = intermediate.pop()
                num1 = intermediate.pop()
                if x == "+":
                    intermediate.append(num1 + num2)
                elif x == "-":
                    intermediate.append(num1 - num2)
                elif x == "*":
                    intermediate.append(num1 * num2)
                else:
                    intermediate.append(int(num1 / num2))
            # if not, push number on the top of the stack
            else:
                intermediate.append(int(x))

        # return the only leftover element in stack
        return intermediate[0]