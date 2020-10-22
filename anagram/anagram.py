

def anagram(str1, str2):
    """ 
    return true/false if anagram
    :param str1: passing is a string
    :param str2: passing String
    :return: true/false
    """
    if len(str1) == len(str2):
        if set(str1) == set(str2):
            return True
        else:
            return False
    else:
        return False
