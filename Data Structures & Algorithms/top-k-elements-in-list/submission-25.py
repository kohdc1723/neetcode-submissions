class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        
        bucket = []
        for _ in range(len(nums) + 1):
            bucket.append([])
        
        for num, count in countMap.items():
            bucket[count].append(num)
        
        res = []
        for nums in reversed(bucket):
            for num in nums:
                res.append(num)
                if len(res) == k:
                    return res