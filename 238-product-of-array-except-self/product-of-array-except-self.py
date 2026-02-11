class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # create an empty array to store the answers
        answers = [1 for i in nums]
        b_prod, a_prod = 1, 1
        length = len(nums)

        # traverse the list once from left to right
        for i in range(0, length, 1):
            # at each step, multiply the previous number
            if i-1 > -1:
                b_prod *= nums[i-1]
            # and assign the result b_prod to the answer array
            answers[i] = b_prod
        
        # traverse the list again from right to left
        for j in range(length-1, -1,-1):
            # at each step, multiply the previous number to get a_prod
            if j+1 < length:
                a_prod *= nums[j+1]
            # update the answer array to contain b_prod * a_prod
            answers[j] *= a_prod

        return answers