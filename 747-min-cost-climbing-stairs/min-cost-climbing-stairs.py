class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # top floor is len(cost) 1st, 2nd, 3rd
        
        def minCost(n, memo={}):
            if n <= 1:
                return 0
            if n in memo:
                return memo[n]
            choice1 = minCost(n-1, memo) + cost[n-1]
            choice2 = minCost(n-2, memo) + cost[n-2]
            memo[n] = min(choice1, choice2)
            return memo[n]

        return minCost(len(cost))
