class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_volume = 0
        while l < r:
            if height[l] < height[r]:
                volume = height[l] * (r - l)
                l += 1
            else:
                volume = height[r] * (r - l)
                r -= 1
            if volume >= max_volume:
                max_volume = volume
        return max_volume
