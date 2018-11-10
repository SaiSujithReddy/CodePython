
import timeit
class Solution:

    def isPalidrome(self, s):
        if s == s[::-1]:
            return True
        return False

    def isNewPalindroem(self, str):
        for i in range(len(str) // 2):
            if str[i] != str[len(str) - i - 1]:
                return False
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_palindrome = ""
        length_palindrome = 0
        counter_length = 0
        counter_length_before = 0
        counter_length_set = 0

        if len(s) == 0:
            return ""
        set_of_all_substrings = set()
        for x in range(len(s)):
            for y in range(x, len(s)):
                #print(s[x:y+1])
                substring = s[x:y+1]
                counter_length_before += 1
                if substring not in set_of_all_substrings:
                    counter_length_set += 1
                    set_of_all_substrings.add(substring)
                    if length_palindrome < len(substring) :
                        counter_length += 1
                        #sorted_substring = "".join(sorted(substring))
                        #print(sorted_substring)
                        #if sorted_substring not in set_of_all_substrings:
                        #    set_of_all_substrings.add(sorted_substring)

                        if self.isNewPalindroem(substring):
                            if length_palindrome < len(substring):
                                length_palindrome = len(substring)
                                longest_palindrome = substring
                            #set_of_all_substrings.add(substring)

        #sorted_by_len = sorted(set_of_all_substrings, key=len, reverse=True)
        print("counter_length_before is ", counter_length_before)
        print("counter_length_set is ", counter_length_set)
        print("counter_length is ", counter_length)
        return longest_palindrome

sol = Solution()
list_z = ["babad", "hello", "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg",
          "gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv"]
for x in list_z:
    #start = timeit.start()
    start_time = timeit.default_timer()
    print(sol.longestPalindrome(x))
    print(timeit.default_timer() - start_time)
    #stop = timeit.stop()
    #print("Total run time ", stop - start)
#timeit.timeit(stmt=foo, number=1234567)

'''

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"


'''

'''
Things i learnt 
Rather than sorting , use two variables to get the longest palindrome substring

'''