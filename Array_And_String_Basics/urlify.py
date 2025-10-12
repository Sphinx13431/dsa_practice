'''
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters,and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
'''

'''
Pesudo code

function(string, TrueLength):
    result_string=''
    for i in range(TrueLength):
        character=string[i]
        if(character ==' '):
            result_string=result_string+'%20'
        else:
            result_string=result_string+character
    return result_string

'''
'''
Best Solution

function count_spaces(urlify:str,urlLength:int)->int:
    count=0
    for i in range(urlLength):
        if(urlify[i]==' '):
            count+=1
    return count

function replace_space(urlify:str, true_length:int)->str:
    actual_length=len(urlify)
    space_count=count_space(urlify,actual_length)
    start,end=0,true_length+2*space_count
    end_copy=end
    char_array=list(urlify)
    for i in range(true_length-1,-1,-1):
        char=char_array[i]
        if(char==' '):
            char_array[end-1]='0'
            char_array[end-2]='2'
            char_array[end-3]='%'
            end-=3
        else:
            char[end-1]=char
            end-=1
    return ''.join()[:end_copy]



'''