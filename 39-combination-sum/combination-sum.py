class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        n = len(candidates)
        def backtrack(start, current):
            val = sum(current)
            # base case: we reach target -> add to results
            if val == target:
                results.append(current[:])
                return
            if val > target or start >= n:
                return
            current.append(candidates[start])
            backtrack(start, current)
            current.pop()
            backtrack(start + 1, current)
        backtrack(0, [])
        return results