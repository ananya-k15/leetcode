class MedianFinder:

    def __init__(self):
        # max heap to store smaller elements
        self.smaller = []
        # min heap to store larger elements
        self.larger = []

    def moveStoL(self, num: int) -> None:
        prev = heapq.heappop(self.smaller) * -1
        heapq.heappush(self.larger, prev)
        heapq.heappush(self.smaller, -1 * num)

    def moveLtoS(self, num: int) -> None:
        prev = heapq.heappop(self.larger) * -1
        heapq.heappush(self.smaller, prev)
        heapq.heappush(self.larger, num)

    def addNum(self, num: int) -> None:
        if self.smaller == []:
            heapq.heappush(self.smaller, -1 * num)
        elif self.larger == []:
            prev = self.smaller[0] * -1
            if prev <= num:
                heapq.heappush(self.larger, num)
                return
            self.moveStoL(num)
        else:
            s, l = self.smaller[0] * -1, self.larger[0]
            if num >= s and num <= l:
                if len(self.smaller) == len(self.larger):
                    heapq.heappush(self.smaller, -1 * num)
                else:
                    heapq.heappush(self.larger, num)
            elif num < s:
                if len(self.smaller) == len(self.larger):
                    heapq.heappush(self.smaller, -1 * num)
                else:
                    self.moveStoL(num)
            else:
                if len(self.smaller) == len(self.larger):
                    self.moveLtoS(num)
                else:
                    heapq.heappush(self.larger, num)

    def findMedian(self) -> float:
        s = self.smaller[0] * -1
        if self.larger == []:
            return s
        elif len(self.smaller) == len(self.larger):
            return (s + self.larger[0]) / 2
        else:
            return s


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()