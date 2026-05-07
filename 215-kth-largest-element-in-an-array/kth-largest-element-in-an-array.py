class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        unique = set()
        heap = []

        for num in nums:
            if num not in unique:
                heapq.heappush(heap, num)

                if len(heap) > k:
                    heapq.heappop(heap)

        return heap[0]