import sys
import string

letters = string.ascii_lowercase
mapping = {}
mapping[' '] = 0
reversed_mapping = {}
reversed_mapping[0] = ' '
for i in range(1,27):
    mapping[letters[i-1]] = i
    reversed_mapping[i] = letters[i-1]

def _encrypt(string):
    string = [mapping[i] for i in string]

    for i in range(1,len(string)):
        string[i] += string[i-1]

    string = [i%27 for i in string]

    return ''.join([reversed_mapping[i] for i in string])

def _decrypt(string):
    string = [mapping[char]+27 if index > 0 else mapping[char] for index, char in enumerate(string)]
    string = [(string[index] - string[index-1])%27 if index > 0 else string[index] for index, chat in enumerate(string)]
    return ''.join([reversed_mapping[i] for i in string])

n = int(input())
for i in range(n):
    line = input()
    operation, string = line[0], line[2:]

    if operation == 'e':
        ans = _encrypt(string)
    else:
        ans = _decrypt(string)
    print(ans)
