class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for i in nums : 
            freq[i] = 1 + freq.get(i, 0)  
        count = {i:[] for i in range(1, len(nums) + 1, 1)}
        for key, value in freq.items() : 
            count[value].append(key)
        topk = []
        # ; ind = len(nums)
        for x in range(len(nums), 0, -1) : 
            for num in count[x] : 
                topk.append(num)
                if len(topk) == k :
                    return topk
        # while dupk != 0 :
        #     topk += count[ind]
        #     dupk -= len(count[ind])
        #     ind -= 1
        return topk
    
        # topk = [l[0] for l in sorted(freq.items(), 
        #                              key=lambda x:x[1], 
        #                              reverse=True)]