'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words
'''
'''
Assumptions
1. All characters are small case English alphabet
2. There are no empty spaces between letters
'''
class Solution:
    def count_ones(self,arr,length)->bool:
        count=0
        for i in range(length):
            if(arr[i]==1):
                count=count+1
        return count <=1
    def is_Palindrome_Permutation(self,s:str)->bool:
        length=len(s)
        char_freq_list=[0]*26
        for i in range(length):
            char=s[i]
            char_index=ord(char)-ord('a')
            if(char_freq_list[char_index]==0):
                char_freq_list[char_index]=char_freq_list[char_index]+1
            else:
                char_freq_list[char_index]=char_freq_list[char_index]-1
        
        return self.count_ones(char_freq_list,26)
    
string1=input("Enter the string:")
myObj=Solution()
if(myObj.is_Palindrome_Permutation(string1)):
    print("It is a valid palindrome permutation")
else:
    print("invalid")