'''
https://www.geeksforgeeks.org/check-possible-transform-one-string-another/

Given two strings s1 and s2(call letters in uppercase). Check if it is possible to convert s1 to s2 by performing following operations.

1. Make some lowercase letters uppercase.
2. Delete all the lowercase letters.

Examples:

Input : s1 = daBcd s2 = ABC
Output : yes
Explanation : daBcd -> dABCd -> ABC
Covert a and b at index 1 and 3 to
upper case, delete the rest those are
lowercase. We get the string s2.

Input : s1 = argaju    s2 = RAJ
Output : yes
Explanation : argaju -> aRgAJu -> RAJ
convert index 1, 3 and 4 to uppercase
and then delete. All lowercase letters

Input : s1 = ABcd s2= BCD
Output : NO


'''


def string_transformation(str1,str2):
    is_possible = False

    if len(str1) < len(str2):
        return is_possible
    else:
        if len(str1) == 1 :
            if str1 == str2 or str1.upper() == str2:
                is_possible = True
        elif len(str2) == 1:
            if str1[0] == str2 or str1[0].upper() == str2:
                is_possible = True
                return is_possible

            else:
                string_transformation(str1[1:],str2)
        elif str1 == str2 or str1.upper() == str2:
                return True
        elif str1[0] == str2[0] or str1[0].upper() == str2[0]:
            string_transformation(str1[1:],str2[1:])
        else:
            string_transformation(str1[1:],str2)

    return is_possible
    #
    # for i in list(str1):
    #     if i == str2[0]:
    #
    #
    # for i,j in zip(list(str1),list(str2)):
    #     if i == j or i.upper() == j:
    #         is_possible = True
    #         i += 1
    #         j += 1
    #     else:
    #         i += 1
    #
    # if j == str2:


str1 = "daBcd"
str2 = "ABC"
print(string_transformation(str1,str2))