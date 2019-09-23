class Solution:
    def lengthOfLongestSubstring(self, string):
        
        
        if len(string) == 0:
            
            return 0
        len_string  = 1
        list_string = []
        for x in string:
            
            if x not in list_string:
                list_string.append(x)
            else:
                
                #print(list_string)
                i = list_string.index(x)
                if len(list_string) > len_string:
                    len_string = len(list_string)
                list_string = list_string[i+1:]
                list_string.append(x)
                #print(list_string)
            if len(list_string) > len_string:
                len_string = len(list_string)
                #print(list_string)
        return len_string
    
    
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) == 0:
#             return 0

#         set_string = set()
#         temp_longest_count =0
#         longest_count =0
#         for x in s:
#             if x in set_string:
#                 if temp_longest_count > longest_count:
#                     longest_count = temp_longest_count
#                     temp_longest_count = 1
#                 else:
#                     temp_longest_count = 1
#             else:
#                 set_string.add(x)
#                 temp_longest_count += 1

#         front_longest = longest_count if longest_count > temp_longest_count else temp_longest_count


sol = Solution()
list_z = ["abcabcbb", "bbbbb", "pwwkew", "dvdf", "asjrgapa"]

for x in list_z:
    print(sol.lengthOfLongestSubstring(x))

'''
It doesn't quite work for use case "asjrgapa"

Things learnt - write a single line python of return statement 
Answer for "asjrgapa" is 6 , we should be careful in counting repeated characters, not alaways the first unique 
substring will be longest

'''
