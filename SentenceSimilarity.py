'''
734. Sentence Similarity

Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.

However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].

'''

words1 = ["great","acting","skills"]
words2 = ["fine","drama","talent"]
#pairs = [["great","fine"],["acting","drama"],["skills","talent"]]
pairs = [["great","fine"],["drama","acting"],["skills","talent"]]

class Solution():
    def checkIfPairExists(self,word1,word2,pairs):
        for x in pairs:
            if x[0] == word1 and x[1] == word2:
                print("Hi1")
                return True
            elif x[1] == word1 and x[0] == word2:
                print("Hi11")
                return True
        print("Hi2")
        return False

    def areSentencesSimilar(self,words1, words2,pairs):

        if len(words1) != len(words2):
            print("Hi3")
            return False

        for x in range(0,len(words1)):
            if words1[x] != words2[x]:
                if(self.checkIfPairExists(words1[x],words2[x],pairs)):
                    print("Hi4")
                    continue
                else:
                    print("Hi5")
                    return False
        return True

obj = Solution()
print(obj.areSentencesSimilar(words1,words2,pairs))
