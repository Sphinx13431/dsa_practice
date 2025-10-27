'''
Given an array of integers heights representing the histogram's bar 
height where the width of each bar is 1, return the area of the largest rectangle 
in the histogram.
Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
'''
#optimal soln
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)  # sentinel to flush stack at the end

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area

#better approach
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        left = [-1] * length
        right = [length] * length
        stack = []

        # previous smaller element
        for i in range(length):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack.clear()

        # next smaller element
        for i in range(length - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # compute max area
        max_area = 0
        for i in range(length):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        return max_area
