class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for i in nums : 
            freq[i] = 1 + freq.get(i, 0)  
        topk = [l[0] for l in sorted(freq.items(), 
                                     key=lambda x:x[1], 
                                     reverse=True)]
        return topk[:k]       
    
        # topk = [l[0] for l in sorted(freq.items(), 
        #                              key=lambda x:x[1], 
        #                              reverse=True)]