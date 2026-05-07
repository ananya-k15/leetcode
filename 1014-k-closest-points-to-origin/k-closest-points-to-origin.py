class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # We maintain a min-heap of fixed size k 
        # to keep track of the k closest points

        heap = []
        # heapq.heapify(heap)

        for x, y in points:
            dist = -1 * (x**2 + y**2)
            heapq.heappush(heap, (dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [x[1] for x in heap]
