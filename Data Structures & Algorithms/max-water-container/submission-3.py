class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) <= 1:
            return 0

        l = 0
        r = len(heights) - 1
        result = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            result = max(result, area)

            if heights[l] < heights[r]:
                l += 1  
            else:
                r -= 1

        return result

        