#A string S is passed as the input. Two words W1 and W2, which are present in the string S are also passed as the input. The program must find the minimum distance D between W1 and W2 in S (in forward or reverse order) and print D as the output.


def distance(sentence,w1,w2):
    if w1 == w2:
        return 0
    words = sentence.split()
    min_dist = len(words) + 1
    for index in range(len(words)):
        if(words[index] == w1):
            for search in range(len(words)):
                if(words[search] == w2):
                    curr = abs(index - search)
                    if curr < min_dist:
                        min_dist = curr
                
    return min_dist

sentence = input().strip()
word1 = input().strip()
word2 = input().strip()
print(distance(sentence,word1,word2))
