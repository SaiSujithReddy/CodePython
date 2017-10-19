import operator

#Print dictionary with next words and their frequencies
def convert_corpus_dict_with_next_word_frequencies(corpus):
    words = corpus.split()
    outerDict = {}

    for i in range(0, len(words) - 1):
        if (outerDict.get(words[i], 0) == 0):
            outerDict[words[i]] = {words[i + 1]: 1}
        else:
            if words[i + 1] in outerDict[words[i]].keys():
                outerDict[words[i]][words[i + 1]] = outerDict[words[i]].get(words[i + 1]) + 1
            else:
                outerDict[words[i]][words[i + 1]] = 1

    print(outerDict)
    return outerDict


#Input = any word
#output = returns a key which has the highest value
def checkMostSuccessiveFrequentWord(input,outerDict):
    if input in outerDict:
        if (len(outerDict[input].keys()) == 1):
            print(outerDict[input].keys()[0])
        else:
            sorted_x = sorted(outerDict[input].items(), key=operator.itemgetter(1),reverse=True)
            print(sorted_x)
            print(sorted_x[0][0])
    else :
        print("Given word is not found in the corpus, Please input correct word")



corpus = "There are functions that take low dimension input and map it onto high dimensional space There are functions are how will are how are how you"
input = "functions"
dictionary = convert_corpus_dict_with_next_word_frequencies(corpus)
checkMostSuccessiveFrequentWord(input,dictionary)