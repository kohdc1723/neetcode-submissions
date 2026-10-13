class Solution:
    # height = [0,2,0,3,1,0,1,3,2,1]
    # maxLeft  [0,0,2,2,3,3,3,3,3,3]
    # maxRight [3,3,3,3,3,3,3,2,1,0]
    def trap(self, height: List[int]) -> int:
        n = len(height)

        leftMax = [0] * n
        rightMax = [0] * n

        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i - 1])
        
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i + 1])
        
        total = 0
        for i in range(n):
            water = min(leftMax[i], rightMax[i]) - height[i]
            if water > 0:
                total += water

        return total