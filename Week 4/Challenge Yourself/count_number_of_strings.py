#To count the number of strings where the string length is 2 or more and the first and last characters are the same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2

def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 2 and word[0] == word[-1]:
      ctr += 1
  return ctr
n=int(input())
words = input().split()
print(match_words(words))
