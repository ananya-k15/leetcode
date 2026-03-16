class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Backtracking solution
        results = [] # list to store all possible string values
        
        # helper function to keep track of possible strings
        def possible(op, cl, paren):
            # if open = number of "(" and close = number of ")"
            # then conditions: open <= n, close <= n and close <= open 
            if op > n or cl > n or cl > op:
                # invalid string, prune
                return
            # if open == close == n -> we have a valid solution
            if op == cl == n:
                results.append(paren)
            # otherwise, we can try adding a open and close parenthesis
            possible(op + 1, cl, paren + '(')
            possible(op, cl + 1, paren + ')')
            return

        possible(0, 0, '')
        return results
