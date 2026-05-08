class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        results = []
        n = len(candidates)
        def backtrack(start, current, val):
            # print(start, current, val)
            # base case: we reach target -> add to results
            if val == target:
                results.append(current[:])
                return
            prev = None
            for x in range(start, n):
                if prev == candidates[x]:
                    continue
                if val + candidates[x] > target:
                    return
                current.append(candidates[x])
                val += candidates[x]
                backtrack(x+1, current, val)
                current.pop()
                val -= candidates[x]
                prev = candidates[x]
        backtrack(0, [], 0)
        return results