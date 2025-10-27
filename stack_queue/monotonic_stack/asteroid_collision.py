'''
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide
'''
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # Ignore 0s (optional)
            if a == 0:
                continue

            # Collision only possible if a < 0 and stack[-1] > 0
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()  # right one explodes
                    continue
                elif stack[-1] == -a:
                    stack.pop()  # both explode
                break
            else:
                # no collision (either stack empty, or same direction)
                stack.append(a)

        return stack