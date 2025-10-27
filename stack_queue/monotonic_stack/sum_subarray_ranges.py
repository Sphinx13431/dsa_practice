'''
You are given an integer array nums. The range of a subarray of nums is the difference 
between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
'''

from typing import List

class Solution:
    def find_next_bigger_element_position(self, arr, length):
        stack = []
        position = [length] * length
        for i in range(length - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                position[i] = stack[-1]
            stack.append(i)
        return position

    def find_prev_bigger_element_position(self, arr, length):
        stack = []
        position = [-1] * length
        for i in range(length):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                position[i] = stack[-1]
            stack.append(i)
        return position

    def sumSubarrayMaxs(self, arr, length):
        next_bigger = self.find_next_bigger_element_position(arr, length)
        prev_bigger = self.find_prev_bigger_element_position(arr, length)

        total = 0
        for i in range(length):
            left = i - prev_bigger[i]
            right = next_bigger[i] - i
            total += arr[i] * left * right
        return total

    def find_next_smaller_element_position(self, arr, length):
        stack = []
        position = [length] * length
        for i in range(length - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                position[i] = stack[-1]
            stack.append(i)
        return position

    def find_prev_smaller_element_position(self, arr, length):
        stack = []
        position = [-1] * length
        for i in range(length):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                position[i] = stack[-1]
            stack.append(i)
        return position

    def sumSubarrayMins(self, arr, length):
        next_smaller = self.find_next_smaller_element_position(arr, length)
        prev_smaller = self.find_prev_smaller_element_position(arr, length)
        total = 0
        for i in range(length):
            left = i - prev_smaller[i]
            right = next_smaller[i] - i
            total += arr[i] * left * right
        return total

    def subArrayRanges(self, nums: List[int]) -> int:
        length = len(nums)
        min_subarray_sum = self.sumSubarrayMins(nums, length)
        max_subarray_sum = self.sumSubarrayMaxs(nums, length)
        return max_subarray_sum - min_subarray_sum