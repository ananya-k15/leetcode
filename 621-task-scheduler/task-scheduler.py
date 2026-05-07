class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        # use a min-heap to keep track of which task 
        # should be used next (the one with the most
        # frequency should be used first)
        heap = {}
        for t in tasks:
            heap[t] = heap.get(t, 0) + 1
        # turn into a list of lists with [freq, val]
        heap = [-1 * v for k, v in heap.items()]
        heapq.heapify(heap)
        # use a queue to figure out when to add back 
        # the removed tasks to the min heap
        queue = deque()
        time = 0
        while len(heap) > 0 or len(queue) > 0:
            time += 1
            if heap == []:
                time = queue[0][0]
            else:
                # remove most frequent task from queue
                freq = heapq.heappop(heap)
                # if freq left, add it to queue with add back time
                freq += 1
                if freq != 0:
                    addBackTime = time + n
                    queue.append((addBackTime, freq))
            # check if top of queue has a freq to be added
            if len(queue) != 0 and queue[0][0] == time:
                _, prevFreq = queue.popleft()
                heapq.heappush(heap, prevFreq)
        return time