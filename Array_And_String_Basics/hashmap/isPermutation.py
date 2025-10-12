'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other
'''
class Solution:
    def isPermutation(self,s1:str,s2:str)->bool:
        len1,len2=len(s1),len(s2)
        #If strings are not of same length
        if (len2 != len1):
            return False
        character_frequency_array=[0]*26

        for c in s1:
            position=ord(c)-ord('a')
            character_frequency_array[position]=character_frequency_array[position]+1

        for c in s2:
            position=ord(c)-ord('a')
            character_frequency_array[position]=character_frequency_array[position]-1
            if character_frequency_array[position]<0:
                return False

        return True
    
s1=input("Enter str1:")
s2=input("Enter str2:")
myObj=Solution()
if(myObj.isPermutation(s1,s2)):
    print("Valid Permutation")
else:
    print("Invalid Permutation")

#Time complexity is O(N)
#Space is O(1)