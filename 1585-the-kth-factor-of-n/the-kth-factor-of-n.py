class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = []
        for x in range(1, n+1):
            if n % x == 0:
                factor.append(x)

        if len(factor) < k:
            return -1
        return factor[k-1]
