'''
you are given an input number as string and a value k. you are allowed to make k 
deletions. find the minimum number that is obtained after k deletion operations. there 
should be no trailing zeroes

ex
input='10200' k=2
result='200'
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        length=len(num)
        if (length==k):
            return '0'
        stack=[]
        stack.append(num[0])
        for i in range(1,length):
            next_dig=num[i]
            #check top of stack is less than or equal to next_dig
            if int(stack[-1])<=int(next_dig):
                stack.append(next_dig)
            
            else:
                while stack and int(stack[-1])>int(next_dig) and k>0:
                    stack.pop()
                    k-=1
                stack.append(next_dig)
        while k > 0 and stack:
            stack.pop()
            k -= 1
        
        # remove leading zeros
        result = ''.join(stack).lstrip('0')
        return result if result else '0'