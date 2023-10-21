
EMPTY_STRING = ''
SPACE_CHAR = ' '
ELLIPSIS = '...'
ELLIPSIS_LEN = 3

#################################################################################
# 1.1 empty, blank, size
#
# - isEmpty(str)                                               - check empty
# - isBlank(str)                                               - check blank
# - size(str)                                                  - length
#
# - equals(str1, str2)
#
# 1.2 normalization
#
# - normalize(str)                                             - trim, '' - > None
# - normalizeSafe(str)                                         - trim, '' - > ''
# - normalizeBlank(str, trimAll, trimBlank)
# ? normalizeQuoted(str)                                       - trim in quoted value: "\' text    \'" - > "\'text\'" 
#
# - emptyIfNone(str)                                           - None -> ''
#
# - noneIfEmpty(str)                                           - '' -> None
# - noneIfEmpty(str, trim)                                     - trim, '' -> None
#
# - defaultIfNone(str, defaultStr)                             - str == None ? defaultStr : str
# - defaultIfEmpty(str, defaultStr)                            - isEmpty(str) ? defaultStr : str
#
# 1.3 trim (left, right)
# 
# - trim(str)                                                  - all trim (left, right)
# - trim(str, ch)
#
# - ltrim(str)                                                 - left trim
# - ltrim(str, ch)
#
# - rtrim(str)                                                 - right trim
# - rtrim(str, ch)
#
# 1.4
#
# - contains(str, substr)
#
# - findFirst(str, substr)
# - findFirst(str, substr, pos)
#
# - findLast(str, substr)
# - findLast(str, substr, pos)
#
#
# - findFirstOf(str, substr)
# - findFirstOf(str, substr, pos)
#
# - findLastOf(str, substr)
# - findLastOf(str, substr, pos)
#
# - findFirstNotOf(str, substr)
# - findFirstNotOf(str, substr, pos)
#
# - findLastNotOf(str, substr)
# - findLastNotOf(str, substr, pos)

#################################################################################
#
#  2.1
#
# - replicate(str, n)                                          - replicate("abc", 3) = "abcabcabc" : repeat (?)
# - replicate(ch, n)                                           - replicate('a', 3) = "aaa"
#
# 2.2
#
# - lpad(str, len)                                             - lpad("abc", 5)      = "  abc"
# - lpad(str, len, pad)                                        - lpad("abc", 5, "*") = "**abc"
#
# - rpad(str, len)                                             - rpad("abc", 5)      = "abc  "
# - rpad(str, len, pad)                                        - rpad("abc", 5, "*") = "abc**"
#
# 2.3
#
# - fill(str, en)
# - fill(str, len, pad)
#
# - ellipsis(str, len)
#
# - trunc(str, len)
# - trunc(str, len, trim, ellipsis)
#
# - left(str, len)
# - right(str, len)

# 1.1

def isEmpty(str):
    if str == None:
        return True    
    return len(str) == 0

def isBlank(str):
    if str == None:
        return True    
    return len(str.strip()) == 0 # trim

def size(str):
    if str == None:
        return 0
    return len(str)

def equals(str1, str2):
    #if str1 == None or str2 == None:
    #    return False    
    return str1 == str2    

# 1.2

def normalize(str):
    if str == None:
        return None
    
    if len(str) == 0:
        return None

    res = str.strip() # trim

    if len(res) == 0:
        return None
    else:
        return res

def normalizeSafe(str):
    if str == None:
        return EMPTY_STRING    
    return str.strip() # trim

def normalizeBlank(str, trimAll, trimBlank):
    if str == None:
        return None

    #if len(str) == 0:
    #    return EMPTY_STRING
    
    if not trimAll and not trimBlank:
        return str
    
    if not trimAll:
        # trimBlank=True, because we have condition (not trimAll and not trimBlank) before
        # Analize blank
        if isBlank(str):
            return None
        else:
            return str
    else:
        return normalize(str)

def emptyIfNone(str):
    if str == None:
        return EMPTY_STRING
    else:
        return str

def noneIfEmpty(str, trim = False):
    if str == None or len(str) == 0:
        return None
    else:
        if trim:
            return str.strip() # trim
        else:
            return str

def defaultIfNone(str, defaultStr):
    if str == None:
        return defaultStr
    else:
        return str

def defaultIfEmpty(str, defaultStr):
    if str == None or len(str) == 0:
        return defaultStr
    else:
        return str

# Null: experimental
#def emptyIfNull(str):
#    return emptyIfNone(str);

#def nullIfEmpty(str):
#    return noneIfEmpty(str)

#def defaultIfNull(str, defaultStr):
#    return defaultIfNone(str, defaultStr)

# 1.3

## trim

def trim(str, ch = None):
    if str == None:
        return None
    return str.strip(ch)

def ltrim(str, ch = None):
    if str == None:
        return None
    return str.lstrip(ch)

def rtrim(str, ch = None):
    if str == None:
        return None
    return str.rstrip(ch)

# 1.4

def contains(str, substr):
    if isEmpty(str) or isEmpty(substr):
        return False

    # '' in ''            = True
    # ''.__contains__('') = True
    # ''.find('')         = 0 (!): str[0] - IndexError
    # ''.find('\0')       = -1
    # ' '.find('')        = 0 (!): str[0] != '' -> ' ' != ''

    # str = ''
    # substr = ''
    # 
    # index = str.find(substr)
    # if index > -1:
    #     str[index]       - IndexError: string index out of range (!)
    #

    # Performance
    #return substr in str            # 0.15
    #return str.__contains__(substr) # 0.25   
    #return str.find(substr) > -1    # 0.30

    return substr in str

def findFirst(str, substr, pos = None):
    if isEmpty(str) or isEmpty(substr):
        return -1

    len = size(str)
    if len == 0:
        return -1

    if pos == None:
        pos = 0 # first index
    
    if pos < 0 or pos >= len:
        return -1
    
    return str.find(substr, pos) # [pos: len]

def findLast(str, substr, pos = None):
    if isEmpty(str) or isEmpty(substr):
        return -1

    len = size(str)
    if len == 0:
        return -1

    if pos == None:
        pos = len - 1 # last index
    
    if pos < 0 or pos >= len:
        return -1
    
    return str.rfind(substr, 0, pos + 1) # [0: pos + 1] exclude last index

def findFirstOf(str, terms, pos = None):
    if isEmpty(str) or isEmpty(terms):
        return -1

    if pos == None:
        pos = 0 # first index

    len = size(str)
    if len == 0:
        return -1
    
    if pos < 0 or pos >= len:
        return -1

    i = pos

    if (len == 1):
        return str.find(terms, pos) # [pos: len]
        #while (i < len):
        #    if (str[i] == terms):
        #        return i
        #    i += 1
    else:
        while (i < len):
            if (contains(terms, str[i])):
                return i
            i += 1

    return -1

def findLastOf(str, terms, pos = None):
    if isEmpty(str) or isEmpty(terms):
        return -1

    len = size(str)
    if len == 0:
        return -1

    if pos == None:
        pos = len - 1 # last index

    if pos < 0 or pos >= len:
        return -1

    i = pos

    if (len == 1):
        return str.rfind(terms, 0, pos + 1) # [0: pos + 1] exclude last index
        #while (i >= 0):
        #    if (str[i] == terms):
        #        return i
        #    i -= 1
    else:
        while (i >= 0):
            if (contains(terms, str[i])):
                return i
            i -= 1

    return -1

def findFirstNotOf(str, terms, pos = None):
    if isEmpty(str) or isEmpty(terms):
        return -1

    if pos == None:
        pos = 0

    len = size(str)
    if len == 0:
        return -1
    
    if pos < 0 or pos >= len:
        return -1

    i = pos

    if (len == 1):
        while (i < len):
            if (str[i] != terms):
                return i
            i += 1
    else:
        while (i < len):
            if (not contains(terms, str[i])):
                return i
            i += 1

    return -1

def findLastNotOf(str, terms, pos = None):
    if isEmpty(str) or isEmpty(terms):
        return -1

    len = size(str)
    if len == 0:
        return -1

    if pos == None:
        pos = len - 1

    if pos < 0 or pos >= len:
        return -1

    i = pos

    if (len == 1):
        while (i >= 0):
            if (str[i] != terms):
                return i
            i -= 1
    else:
        while (i >= 0):
            if (not contains(terms, str[i])):
                return i
            i -= 1

    return -1


# 2.1

def replicate(str, n):
    if str == None:
        return None
    
    if n < 1:
        return str

    return str * n

# 2.2

def lpad(str, len, pad = ' '):
    if str == None:
        return None
    
    if len < 1 or pad == None:       # pad == None: no padding
        return str
        
    padLen = size(pad)
    if padLen == 1:
        return str.rjust(len, pad)   # lpad = rjust for padlen = 1
    
    strLen = size(str)
    if len <= strLen or padLen == 0: # padLen == 0: no padding
        return str
    
    fillLen = len - strLen
    padCount = fillLen // padLen

    if fillLen % padLen > 0:
        padCount = padCount + 1

    fillStr = replicate(pad, padCount)

    if size(fillStr) > fillLen:
        return fillStr[:fillLen] + str
    else:
        return fillStr + str

def rpad(str, len, pad = ' '):
    if str == None:
        return None
    
    if len < 1 or pad == None:       # pad == None: no padding
        return str
        
    padLen = size(pad)
    if padLen == 1:
        return str.ljust(len, pad)   # rpad = ljust for padlen = 1
    
    strLen = size(str)
    if len <= strLen or padLen == 0: # padLen == 0: no padding
        return str
    
    fillLen = len - strLen
    padCount = fillLen // padLen

    if fillLen % padLen > 0:
        padCount = padCount + 1

    fillStr = replicate(pad, padCount)

    if size(fillStr) > fillLen:
        return str + fillStr[:fillLen]
    else:
        return str + fillStr

def fill(str, len, pad = ' '):
    if str == None or len < 1:
        return EMPTY_STRING
    
    strLen = size(str)
    if strLen == len:
        return str
    
    if strLen < len:
        # add <pad> to right side
        return rpad(str, len, pad)
    else:
        # remove chars from right side
        return trunc(str, len, False, True)

def ellipsis(str, len):
    return trunc(str, len, False, True)

def trunc(str, len, trim = False, ellipsis = False):
    if str == None:
        return None
    
    if len < 1:
        return str
    
    if trim:
        str = str.strip() # trim

    if size(str) <= len:
        return str
    
    if ellipsis:
        if len <= ELLIPSIS_LEN:
            return str[:len]
        else:
            return str[:len - ELLIPSIS_LEN] + ELLIPSIS
    else:
        return str[:len]
    
def left(str, len):
    if str == None:
        return None
        
    strLen = size(str)
    if strLen <= len:
        return str
    else:    
        return str[:len]

def right(str, len):
    if str == None:
        return None
        
    strLen = size(str)
    if strLen <= len:
        return str
    else:    
        return str[strLen - len:]
