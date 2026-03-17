class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # use two pointers to traverse the list
        i, j = 0, len(numbers)-1

        while True:
            current = numbers[i] + numbers[j]
            if current == target:
                return [i+1, j+1]
            elif current < target:
                i += 1
            else:
                j -= 1

        
