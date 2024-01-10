# https://leetcode.com/problems/trapping-rain-water/description/

# Beats 73.65 % (neetcode copied)

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) -1
        maxL, maxR = height[l], height[r]
        while l < r :
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]

        return res