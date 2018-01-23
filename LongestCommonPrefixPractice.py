# Don't try dictionary all the times
# try zip / enumerate


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for index, ch in shortest:
        for string in strs:
            if string[index] != ch:
                return shortest[:index]
    return shortest

    # new_strs = []
    # for x in strs:
    #     new_strs.append(list(x))
    #
    # dict_strs = {}
    # for x in strs:
    #     dict_strs[x] = len(x)
    #
    # min_length = min(dict_strs, key=len)
    #
    # temp_str = None


list_of_strings = ['hello','hell','hei']
print(longestCommonPrefix(list_of_strings))
