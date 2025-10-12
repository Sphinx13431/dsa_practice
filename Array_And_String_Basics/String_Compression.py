'''
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''

'''
Clarifying qns
do we treat lower and upper case as equal( a= A)?
can the string be an empty string
'''

class Solution:
    def string_compression(self, string1:str)->str:
        if(string1 == ''):
            return ''
        length=len(string1)
        result=''
        prev_char,counter=string1[0],1

        for i in range(1,length):
            curr_char=string1[i]
            if(prev_char == curr_char):
                counter+=1
            else:
                result+=prev_char+''+str(counter)
                prev_char=curr_char
                counter=1
        result += prev_char + str(counter)

        # Return original if not smaller
        return result if len(result) < len(string1) else string1 

str1=input("Enter the string")
myObj=Solution()
print(myObj.string_compression(str1))
