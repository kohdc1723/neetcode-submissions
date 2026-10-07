class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            diff = target - n
            
            if n in map:
                return [map[n], i]
            
            map[diff] = i