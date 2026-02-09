class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dict to store {num : frequency}
        frequency = dict()

        # loop through each number in nums
        for num in nums:
            # add it to the dictionary or update frequency
            frequency[num] = frequency.get(num, 0) + 1

        # sort the dictionary by values using a custom lambda function
        freq_sorted = sorted(frequency.items(), key=(lambda item: item[1]), reverse=True)

        # we get a list of tuples [(nums, freq)] ordered by freq
        # pick the top k nums and return
        freq_sorted = freq_sorted[:k]
        return [x[0] for x in freq_sorted]


