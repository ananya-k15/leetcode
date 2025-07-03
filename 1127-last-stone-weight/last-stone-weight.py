class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        modified_stones = [-1*x for x in stones]
        heapify(modified_stones)

        while len(modified_stones) > 1:
            x = heappop(modified_stones)
            y = heappop(modified_stones)

            if x != y:
                new_stone = -1 * abs(x-y)
                heappush(modified_stones, new_stone)

        if len(modified_stones) == 0:
            return 0
        return -1*modified_stones[0]