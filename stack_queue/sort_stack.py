'''
Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements into 
any other data structure (such as an array). The stack supports the following
operations:  push, pop, peek, and is Empty.
'''
from typing import List
class solution:
    def sort_stack(stack:List[int])->List[int]:
        temp_stack= list()

        while(stack):
            temp=stack.pop()
            while temp_stack and temp_stack[-1]>temp:
                stack.append(temp_stack.pop())
            temp_stack.append(temp)
        return temp_stack