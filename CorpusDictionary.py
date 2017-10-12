corpus = "There are functions that take low dimension input and map it onto high dimensional space There are functions"

#dict = {}

words = corpus.split()
print(words)

# Print words from a sentence in dictionary by frequency
myDict = {}
for word in words:
    myDict[word] = myDict.get(word,0) +1
print(myDict)