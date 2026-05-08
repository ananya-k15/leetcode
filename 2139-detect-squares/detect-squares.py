class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.points[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        count = 0

        # we need to find the length of the edge
        # if a point has the same x coordinate as query point
        x, y = point[0], point[1]
        for p in self.points[x]:
            if y == p:
                continue
            d = abs(y - p)

            # look at all the possible y coordinates
            # compute edge length = y - point[1]
            # if the corresponding points exist, get their freqs
            # multiple frequencies and add to count
            if self.points[x+d].get(y, 0) != 0:
                if self.points[x+d].get(p, 0) != 0:
                    count += self.points[x][p] * self.points[x+d][y] * self.points[x+d][p]

            if self.points[x-d].get(y, 0) != 0:
                if self.points[x-d].get(p, 0) != 0:
                    count += self.points[x][p] * self.points[x-d][y] * self.points[x-d][p]

        return count
        
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)