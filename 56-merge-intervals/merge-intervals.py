class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Edgecase: There is only one interval
        # It's non overlapping by default
        if len(intervals) == 1:
            return intervals

        intervals = sorted(intervals, key = lambda x: x[0])

        # We have a list of intervals [a, b] [c, d]
        # We want to merge them if b > c. 
        # Otherwise, they are overlapping.
        # We can do this by using two pointers
        first, second = 0, 1

        while second < len(intervals):
            if intervals[first][1] >= intervals[second][0]:
                intervals[first][1] = max(intervals[second][1], intervals[first][1])
                second += 1
            else:
                first += 1
                intervals[first] = intervals[second]
                second += 1

        return intervals[:first+1]