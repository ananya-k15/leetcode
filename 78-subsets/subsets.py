class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        # we can use recursive backtracking to solve this
        def backtrack(index, current):
            print(current)
            nonlocal results
            # at each node of the decision tree,
            # add the result to the results list
            results.append(current[:]) # snapshot copy
            # choose a number from num[index:] to add to the current result
            for ind in range(index, len(nums)):
                current.append(nums[ind])
                # recurse on that iteration
                backtrack(ind+1, current)
                # undo the choice before moving on to the next
                current.pop()

        backtrack(0, [])
        return results