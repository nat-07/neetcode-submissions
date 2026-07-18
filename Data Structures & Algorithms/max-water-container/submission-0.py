class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        highestArea = min(heights[left], heights[right])* (right-left)
        while left < right: 
            if (left+1 == right):
                return highestArea
            if (heights[left] < heights[right]): 
                left+= 1
            else:
                right-= 1        
            area = (min(heights[left], heights[right]))*(right-left)
            if (highestArea < area): 
                highestArea = area