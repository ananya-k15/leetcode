class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        part1 = nums[:n]
        part2 = nums[n:]
        new = []
        for i in range(0, n, 1) :
            new.append(part1[i])
            new.append(part2[i])
        return new
        