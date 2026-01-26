class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # k must lie between 1 and max(piles)
        # let's use binary search to find the least possible value of k

        l, r = 1, max(piles) # 0, 30
        res = max(piles)

        while l < r: # 29 < 30
            mid = (l + r) // 2 # 29

            time = sum([ceil(x/mid) for x in piles]) # 2 + 1 + 1 + 1 + 1 # 6

            if time > h: # 6 > 5
                # we need to increase k to reach h
                l = mid + 1 # 30
            else:
                # we need to decrease k
                r = mid 
                res = mid 
        
        return res