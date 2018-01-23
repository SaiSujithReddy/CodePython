'''

Main Technical Question: Write a function that takes as input an array of words
input => ['cat', 'star', 'act', 'god', 'arts', 'dog', 'rats']
and returns a sorted array
output => ['cat', 'act', 'god', 'dog', 'start', 'arts', 'rats']

'''

input = ['cat', 'star', 'act', 'god', 'arts', 'dog', 'rats']

print(sorted(input,key=lambda x:sorted(x)))