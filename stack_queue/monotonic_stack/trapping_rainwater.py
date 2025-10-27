'''
Given n non-negative integers representing an elevation map where the width of each 
bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being 
'''
from typing import List
class Solution:

    def find_max_left_height(self,arr:List[int],length:int)->List[int]:
        for i in range(1,length):
            arr[i]=max(arr[i-1],arr[i])
        return arr

    def find_max_right_height(self,arr:List[int],length:int)->List[int]:
        for i in range(length-2,-1,-1):
            arr[i]=max(arr[i+1],arr[i])
        return arr

    def trap(self, height: List[int]) -> int:
        '''
        for a given building find the tallest building at left and right wrt that building'''
        length=len(height)
        left=height.copy()
        right=height.copy()
        lmax=self.find_max_left_height(left,length)
        rmax=self.find_max_right_height(right,length)
        total_water_trapped=0
        for i in range(length):
            total_water_trapped+=min(lmax[i],rmax[i])-height[i]
        return total_water_trapped