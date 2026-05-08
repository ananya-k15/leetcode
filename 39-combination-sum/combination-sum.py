class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        n = len(candidates)
        def backtrack(start, current, val):
            # base case: we reach target -> add to results
            if val == target:
                results.append(current[:])
                return
            if val > target or start >= n:
                return
            current.append(candidates[start])
            backtrack(start, current, val + candidates[start])
            current.pop()
            backtrack(start + 1, current, val)
        backtrack(0, [], 0)
        return results