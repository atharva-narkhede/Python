#Dr. Nadal is given a string of ‘n’ characters(S[1], S[2],...., S[n]).
def check_palindrome(string,start,end):
    check_string = string[start:end]
    if(check_string[::] == check_string[::-1]):
        print("YES")
    else:
        print("NO")

string = input()
n = int(input())
for i in range(n):
    [start,end] = [int(i) for i in input().split()]
    check_palindrome(string,start-1,end)
