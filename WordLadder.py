'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

'''


from collections import deque



def ladderLength(beginWord, endWord, word_list):
    pass

def construct_dict(word_list):
    d = {}
    for word in word_list:
        for i in range(len(word)):
            s = word[:i] + "_" + word[i + 1:]
            d[s] = d.get(s, []) + [word]
            # d.get(s, []) --> gets d[s] and if not found takes [] as default value

    for x in d:
        print(x,d[x])
    return d

def bfs_words(begin, end, dict_words):
    queue, visited = deque([(begin, 1)]), set()
    while queue:
        word, steps = queue.popleft()
        if word not in visited:
            visited.add(word)
            if word == end:
                return steps
            for i in range(len(word)):
                s = word[:i] + "_" + word[i + 1:]
                neigh_words = dict_words.get(s, [])
                for neigh in neigh_words:
                    if neigh not in visited:
                        queue.append((neigh, steps + 1))
    return 0

#d = construct_dict(wordList | set([beginWord, endWord]))
#return bfs_words(beginWord, endWord, d)

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
ladderLength(beginWord,endWord,wordList)
print(bfs_words(beginWord, endWord, construct_dict(wordList)))