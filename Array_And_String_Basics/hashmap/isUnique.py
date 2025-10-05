'''is Unique: Implement an algorithm to determine if a string has all unique characters. What if you 
cannot use additional data structures? '''

class Solution:
    def isUnique(self,s:str)->bool:
        my_set=set()
        for c in s:
            if c in my_set:
                return False
            else:
                my_set.add(c)
        return True


input_string=input("Enter the string:")
myobj= Solution()
if(myobj.isUnique(input_string)):
    print("The string has unique characters")
else:
    print("The string does not have unique characters")
    

#Time complexity is: O(N)
#Space Complexoty is:O(1)