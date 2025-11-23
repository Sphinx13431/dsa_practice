'''
Given an array of integers arr, find the sum of min(b), 
where b ranges over every (contiguous) subarray of arr. Since the answer may be large,
return the answer modulo 109 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
'''
from typing import List
class Solution:

    def find_next_smaller_element_position(self,arr:List[int],length:int)->List[int]:
        stack=[]
        position=[length]*length
        for i in range(length-1,-1,-1):
            curr_ele=arr[i]

            while stack and arr[stack[-1]]>curr_ele:
                stack.pop()
            
            if stack:
                position[i]=stack[-1]
            stack.append(i)
        return position

    def find_prev_smaller_element_position(self,arr:List[int],length:int)->List[int]:
        stack=[]
        position=[-1]*length
        for i in range(length):
            curr_ele=arr[i]

            while stack and arr[stack[-1]]>=curr_ele:
                stack.pop()
            
            if stack:
                position[i]=stack[-1]
            stack.append(i)
        return position


    def sumSubarrayMins(self, arr: List[int]) -> int:
        length=len(arr)
        mod=10**9+7
        next_smaller_element_index=self.find_next_smaller_element_position(arr,length)
        prev_smaller_element_index=self.find_prev_smaller_element_position(arr,length)
        total=0
        for i in range(length):
            left=i-prev_smaller_element_index[i]
            right=next_smaller_element_index[i]-i
            total = (total + arr[i] * left * right) % mod
        return total

        