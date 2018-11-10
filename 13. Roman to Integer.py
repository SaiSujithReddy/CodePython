class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary_roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        length_string = len(s)
        i = 0
        total_sum = 0

        for x in range(len(s)):
            if i == length_string-1:
                #print("value of iiiii ", i)
                total_sum += dictionary_roman[s[x]]
                return total_sum
            else:
                # print(x)
                # print(s[x])
                # print(dictionary_roman[s[x]])
                # print("value of i ", i)
                if dictionary_roman[s[x]] < dictionary_roman[s[x+1]]:
                    total_sum -= dictionary_roman[s[x]]
                else:
                    total_sum += dictionary_roman[s[x]]
            i += 1

        #return total_sum


sol = Solution()
x_list = ["III", "IV","IX","LVIII","MCMXCIV"]

for x in x_list:
    print(sol.romanToInt(x))