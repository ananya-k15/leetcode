class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack to track parentheses
        stack = []
        # use a dict to look up parenthesis pairs
        pairs = {']':'[', '}':'{', ')':'('}

        for x in s:
            # if x is an opening parenthesis
            if x in "({[":
                # add it to the stack
                stack.append(x)
            # if it's a closing parenthesis
            else:
                # get the equivalent pair from pairs dict
                opening = pairs[x]
                # check if it's at the top of the stack
                if len(stack) > 0 and stack[-1] == opening:
                    stack.pop()
                # if not, we've found an invalid sequence
                else:
                    return False

        # if stack is empty, the sequence was valid
        return len(stack) == 0