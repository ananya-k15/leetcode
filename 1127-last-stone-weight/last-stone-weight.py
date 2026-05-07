class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # we multiply all the values in stones with -1
        # to create a max-heap using heapq

        stoneHeap = [-1 * x for x in stones]
        heapq.heapify(stoneHeap)

        while len(stoneHeap) > 1:
            x = heapq.heappop(stoneHeap)
            y = heapq.heappop(stoneHeap)

            if x == y:
                continue
            heapq.heappush(stoneHeap, -1 * abs(x-y))

        return 0 if len(stoneHeap) == 0 else -1 * stoneHeap[0]