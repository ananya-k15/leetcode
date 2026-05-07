class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Create a min-heap of size k, and whenever
        # the heap size exceeds k remove the smallest 
        # element -> this effectively stores the kth
        # largest elements

        self.size = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > self.size:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.size:
            heapq.heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)