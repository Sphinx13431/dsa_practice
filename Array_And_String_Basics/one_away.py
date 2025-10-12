'''
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
'''

'''
pale   ple
'''

class Solution:
    def is_one_edit_away(self,s1:str,s2:str)->bool:
        len1,len2=len(s1),len(s2)
        if(len1<len2):
            return self.is_one_edit_away(s2,s1)
        edit_count=0
        i,j=len1-1,len2-1
        while(i>=0 and j>=0):
            if(s1[i]==s2[j]):
                j=j-1
            else:
                edit_count=edit_count+1
            i=i-1
        return edit_count<=1

s1=input("Enter the first str:")
s2=input("Enter the second string:")
myObj=Solution()
if(myObj.is_one_edit_away(s1,s2)):
    print("Yes")
else:
    print("No")