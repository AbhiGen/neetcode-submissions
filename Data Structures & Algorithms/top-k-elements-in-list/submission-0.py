class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1) ]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for i,j in count.items():
            freq[j].append(i)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
