class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            diff = target - n
            
            if n not in map:
                map[diff] = i
            else:
                return [map[n], i]
                