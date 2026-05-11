class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = []
        heapq.heapify(factor)
        for x in range(1, n+1):
            if n % x == 0:
                heapq.heappush(factor, -x)
                if len(factor) > k:
                    heapq.heappop(factor)

        if len(factor) < k:
            return -1
        return -1 * factor[0]
