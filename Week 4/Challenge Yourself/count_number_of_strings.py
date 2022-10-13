#To count the number of strings where the string length is 2 or more and the first and last characters are the same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2

n = str(input())
count = 0
string_list = input().split()
for string in string_list:
    if len(string) >= 2 and string[0] == string[len(string)-1]:
        count+=1
print(count)