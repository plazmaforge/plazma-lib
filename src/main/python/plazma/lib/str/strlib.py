
EMPTY_STRING = ''
SPACE_CHAR = ' '
ELLIPSIS = '...'
ELLIPSIS_LEN = 3

DEFAULT_SEPARATORS = ' \t\n\r\f\v'
DEFAULT_WORD_SEPARATORS = DEFAULT_SEPARATORS + ".,;'(){}[]!?+/=<>*&^%$#@`~|\\"

DEFAULT_CASE_SEPARATOR = '_'
DEFAULT_CASE_SEPARATORS_ = ' -_'
DEFAULT_CASE_SEPARATORS_A = ' -_A'
DEFAULT_ALTER_CASE_SEPARATOR = '-' # XML    
DEFAULT_SNAKE_CASE_SEPARATOR = '_' # SNAKE
DEFAULT_KEBAB_CASE_SEPARATOR = '-' # KEBAB

####################################
# Case Operations
####################################
# caseOp =  1: 'myname': LOWER 
# caseOp =  2: 'MYNAME': UPPER 
# caseOp =  3: 'myName': LOWER_CHAR
# caseOp =  4: 'MyName': UPPER_CHAR    

CO_NONE       = 0
CO_LOWER      = 1
CO_UPPER      = 2
CO_LOWER_CHAR = 3
CO_UPPER_CHAR = 4
#
CO_COUNT      = 4

####################################
# Case Types
####################################
# -  1. lowercase
# -  2. UPPERCASE
# -  3. camelCase
# -  4. CamelCase, PascalCase
# -  5. snake_case
# -  6. SNAKE_CASE, MACRO_CASE, CONSTANT_CASE
# -  7. Snake_Case
# -  8. kebab-case, dash-case, train-case, lisp-case
# -  9. KEBAB-CASE, DASH-CASE, TRAIN-CASE, COBOL-CASE
# - 10. Kebab-Case, Dash-Case, Train-Case, HTTP-Header-Case

CT_NONE       = 0
CT_lowercase  = 1
CT_UPPERCASE  = 2
CT_camelCase  = 3
CT_PascalCase = 4
CT_snake_case = 5
CT_SNAKE_CASE = 6
CT_Snake_Case = 7
CT_kebab_case = 8
CT_KEBAB_CASE = 9
CT_Kebab_Case = 10
#
CT_COUNT      = 10

SNAKE_CONNECTOR = '_' # shake_case
KEBAB_CONNECTOR = '-' # kebab-case

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
#
# - defaultIfNone(str, defaultStr)                             - str is None ? defaultStr : str
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
# - trimElements(elements)
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
# 2.1
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
# - trunc(str, len, ellipsis)
#
# - left(str, len)
# - right(str, len)

#################################################################################
#
# 3.1
#
# - capitalize(str, forceRest)  
# - decapitalize(str, forceRest)
#
# - upper(str)
# - lower(str)
#
# - toUpperCase(str)
# - toLowerCase(str)
#
# - toCase(str, upper)
#
# - toCamelCase(str, separators, capitalize)
# - toSnakeCase(str, separators, upper)
# - toKebabCase(str, separators, upper)
#
#  - reverse(str)                                                     - reverse("abc") = "cba"

#################################################################################
#
# 4.1
#
# - startsWith(str, prefix)                                           - startsWith("myfile.txt", "myfile") = True
# - startsWithIgnoreCase(str, prefix)                                 - startsWithIgnoreCase("myfile.txt", "MyFile") = True
#
# - endsWith(str, suffix)                                             - endsWith("myfile.txt", ".txt") = True
# - endsWithIgnoreCase(str, suffix)                                   - endsWithIgnoreCase("myfile.txt", ".TxT") = True
#
# - hasPrefix(str, prefix)                                            - [alias]: hasPrefix("myfile.txt", "myfile") = True
# - hasPrefixIgnoreCase(str, prefix)                                  - [alias]: hasPrefixIgnoreCase("myfile.txt", "MyFile") = True

# - hasSuffix(str, suffix)                                            - [alias]: hasSuffix("myfile.txt", ".txt") = True
# - hasSuffixIgnoreCase(str, suffix)                                  - [alias]: hasSuffixIgnoreCase("myfile.txt", ".TxT") = True
#
# 4.2
#
# - removePrefix(str, prefix)
# - removePrefixes(str, prefixes)
#
# - removeSuffix(str, suffix)
# - removeSuffixes(str, suffixes)
#
# 4.3
# 
# - isQuoted(str)
# - isQuoted(str, start, end)
#
# - needQuote(str)
# - needQuote(str, start, end)
#
# - quote(str)
# - quote(str, start, end)
#
# - unquote(str)
# - unquote(str, start, end)
#
# 4.4
# 
# - isColumnSeparator(ch)
#
# - isColumnText(str)
# - isColumnText(str, len)
#
# - isLineText(str)
# - isLineText(str, len)

#################################################################################
#    
# 5.1
#
# - countChars(str, ch)
# - countStrings(str, substr)
#
# - countWords(str)
# - countWords(str, separators)
# - countLines(str)
#

#################################################################################
# 6.1
#  
# - replaceAll(str, s1, s2)
# - replaceAll(str, values1, values2)
# - replaceAll(str, map)

#################################################################################
# 7.1
#
# - split(str)
# - split(str, separator)
#    
# - splitBySeparator(str, separator)
# - splitBySeparator(str, separator, preserveAll)
#
# - splitBySeparators(str, separators)
# - splitBySeparators(str, separators, preserveAll)
#
# - splitTrim(str)
# - splitTrim(str, separator)
#
# - splitTrimBySeparator(str, separator)
#
# - splitTrimBySeparators(str, separators)
#
# - splitWords(str)
# - splitWords(str, separator)
# - splitLines(str)
#    
# - tokenizeBySeparator(str, separator)
# - tokenizeBySeparator(str, separator, includeAll, preserveAll)
#
# - tokenizeBySeparators(str, separators)
# - tokenizeBySeparators(str, separators, includeAll, preserveAll)

# 1.1

def isEmpty(str):
    if str is None:
        return True    
    return len(str) == 0

def isBlank(str):
    if str is None:
        return True    
    return len(str.strip()) == 0 # trim

def size(str):
    if str is None:
        return 0
    return len(str)

def equals(str1, str2):
    return str1 == str2    

# 1.2

def normalize(str):
    if str is None:
        return None
    
    if len(str) == 0:
        return None

    res = str.strip() # trim

    if len(res) == 0:
        return None
    else:
        return res

def normalizeSafe(str):
    if str is None:
        return EMPTY_STRING    
    return str.strip() # trim

def normalizeBlank(str, trimAll, trimBlank):
    if str is None:
        return None
   
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
    if str is None:
        return EMPTY_STRING
    else:
        return str

def noneIfEmpty(str):
    if isEmpty(str):
        return None
    return str

def defaultIfNone(str, defaultStr):
    if str is None:
        return defaultStr
    else:
        return str

def defaultIfEmpty(str, defaultStr):
    if isEmpty(str):
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
    if str is None:
        return None
    return str.strip(ch)

def trimSpace(str):
    return trim(str, SPACE_CHAR)

def trimAll(str):
    return trim(str, None)

##

def ltrim(str, ch = None):
    if str is None:
        return None
    return str.lstrip(ch)

def ltrimSpace(str):
    return ltrim(str, SPACE_CHAR)

def ltrimAll(str):
    return ltrim(str, None)

##

def rtrim(str, ch = None):
    if str is None:
        return None
    return str.rstrip(ch)

def rtrimSpace(str):
    return rtrim(str, SPACE_CHAR)

def rtrimAll(str):
    return rtrim(str, None)

##

def trimElements(elements):
    if isEmpty(elements):
        return
    
    for i, element in enumerate(elements):
        elements[i] = trim(element)

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

    if (size(terms) == 1):
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

    if (size(terms) == 1):
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

    if (size(terms) == 1):
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

    if (size(terms) == 1):
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
    if str is None:
        return None
    
    if n < 1:
        return EMPTY_STRING

    return str * n

# 2.2

def lpad(str, len, pad = ' '):
    if str is None:
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
    if str is None:
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

# 2.3

def fill(str, len, pad = ' '):
    if str is None:
        return None
    
    # hard format: <=len or empty
    if len < 1:
        return EMPTY_STRING
    
    strLen = size(str)
    if strLen == len:
        return str
    
    # hard format: pad or trunc    
    if strLen < len:
        # add <pad> to right side
        return rpad(str, len, pad)
    else:
        # remove chars from right side
        return trunc(str, len, True) # ellipsis

def ellipsis(str, len):
    return trunc(str, len, True) # ellipsis

def trunc(str, len, ellipsis = False):
    if str is None:
        return None

    # soft format    
    if len < 1:
        return str
    
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
    if str is None:
        return None
    
    # hard format: <=len or empty
    if len < 1:
        return EMPTY_STRING

    strLen = size(str)
    if strLen <= len:
        return str
    else:    
        return str[:len]

def right(str, len):
    if str is None:
        return None

    # hard format: <=len or empty
    if len < 1:
        return EMPTY_STRING

    strLen = size(str)
    if strLen <= len:
        return str
    else:    
        return str[strLen - len:]

# 3.1

def capitalize(str, forceRest = False):
    if isEmpty(str):
        return str
    
    # return str.capitalize()
    # str[0:1].upper() + str[1:].lower()
    # return ''.join([str[:1].lower(), (str[1:].upper() if upper_rest else str[1:])])

    # if 'forceRest' then lower rest
    return ''.join([str[0].upper(), (str[1:].lower() if forceRest else str[1:])])
    
def decapitalize(str, forceRest = False):
    if isEmpty(str):
        return str

    # if 'forceRest' then upper rest
    return ''.join([str[0].lower(), (str[1:].upper() if forceRest else str[1:])])

def upper(str):
    return toUpperCase(str)

def lower(str):
    return toLowerCase(str)

def toUpperCase(str):
    if str is None:
        return None
    return str.upper()

def toLowerCase(str):
    if str is None:
        return None
    return str.lower()

def toCase(str, upper):
    if str is None:
        return None
    if upper:
        return str.upper()
    else:
        return str.lower()
####

def toIgnoreCase(str):
    return toLowerCase(str)

####

def toCamelCase(str, separators = None, capitalize = True):
    type = 'Camel' if capitalize else 'camel'
    return _toTypeCase(str, type, separators, None)

def toSnakeCase(str, separators = None, upper = False):
    type = 'SNAKE' if upper else 'snake'
    return _toTypeCase(str, type, separators, SNAKE_CONNECTOR)

def toKebabCase(str, separators = None, upper = False):
    type = 'KEBAB' if upper else 'kebab'
    return _toTypeCase(str, type, separators, KEBAB_CONNECTOR)

##################################################################
# Internal
##################################################################

def _splitOp(str, separators):
    result = []

    if isEmpty(str) or isEmpty(separators):
        result.append(str)
        return result

    strLen = len(str)
    sepLen = len(separators)

    ch = ''
    separator = ''
    find = False

    pos = 0
    end = 0
    i = 0
    j = 0

    while i < strLen:

        ch = str[i]
        find = False
        j = 0

        # Find a separator
        while j < sepLen:
            separator = separators[j]
            if separator == 'A': # TODO: 'A' is special marker for check 'Upper Char'
                if ch.isupper():
                    find = True
                    break
                    
            elif ch == separator:
                find = True
                break
            j += 1

        if find:
            end = i

            if pos < end:
                result.append(str[pos:end])

            if separator == 'A': # TODO: 'A' is special marker for check 'Upper Char'
                pos = end     # include 'Upper Char'
            else:
                pos = end + 1 # skip separator

        i += 1
                
    if pos < strLen:
        result.append(str[pos:])

    return result

# Transform token
def _transformToken(token, caseOp, first):
    if isEmpty(token):
        return token
    
    if caseOp == CO_LOWER_CHAR:                 # camelCase
        if first:
            return token[0].lower() + token[1:] # lower char (first)
        else:
            return token[0].upper() + token[1:] # UPPER char (first)

    elif caseOp == CO_UPPER_CHAR:               # CamelCase, PascalCase
        return token[0].upper() + token[1:]     # UPPER char (first)

    elif caseOp == CO_LOWER:  
        return token.lower()                    # lower case

    elif caseOp == CO_UPPER:
        return token.upper()                    # UPPER case

    return token

# Transformation tokens by caseOp
def _transformOp(tokens, caseOp):
    if tokens is None:
        return

    if len(tokens) == 0:
        return

    # No transformation
    if caseOp == CO_NONE:
        return
        
    for i, token in enumerate(tokens):
        tokens[i] = _transformToken(token, caseOp, i == 0)

# caseOp =  1: 'myname': LOWER
# caseOp =  2: 'MYNAME': UPPER
# caseOp =  3: 'myName': LOWER_CHAR
# caseOp =  4: 'MyName': UPPER_CHAR
def _toCaseOp(str, separators, connector, caseOp):
    if isBlank(str):
        return str
        
    result = '' 
    tokens = _splitOp(str, separators)

    #print("str=", str)
    #print("inp=", tokens)
    _transformOp(tokens, caseOp)
    #print("out=", tokens)

    hasConnector = not isEmpty(connector)

    for i in range(0, len(tokens)):
        if i > 0 and hasConnector:
            result = result + connector
        
        result = result + tokens[i]

    return result

# -  1. lowercase, [lower]~
# -  2. UPPERCASE, [upper]~
# -  3. camelCase, [camel]~
# -  4. CamelCase, PascalCase, [pascal]~
# -  5. snake_case, [snake]
# -  6. SNAKE_CASE, MACRO_CASE, CONSTANT_CASE, [SNAKE], [macro]~
# -  7. Snake_Case, [Snake]
# -  8. kebab-case, dash-case, train-case, lisp-case, [kebab]
# -  9. KEBAB-CASE, DASH-CASE, TRAIN-CASE, COBOL-CASE, [KEBAB], [cobol]~
# - 10. Kebab-Case, Dash-Case, Train-Case, HTTP-Header-Case, [Kebab], [http]~

# caseOp =  1: 'myname': LOWER
# caseOp =  2: 'MYNAME': UPPER
# caseOp =  3: 'myName': LOWER_CHAR
# caseOp =  4: 'MyName': UPPER_CHAR
def _toTypeCase(str, type, separators, connector):

    if isEmpty(str):
        return str

    code = getCaseCode(type)
    if code == 0:
        # Invalid case code
        return str        

    # SIMPLE CASE
    if code == CT_lowercase:
        return toCase(str, False) # lower case
    elif code == CT_UPPERCASE:
        return toCase(str, True)  # UPPER case

    # COMPLEX CASE
    _separators = (DEFAULT_CASE_SEPARATORS_A if isEmpty(separators) else separators)

    _connector = connector
    if code == CT_kebab_case or code == CT_KEBAB_CASE or code == CT_Kebab_Case:
        _connector = (KEBAB_CONNECTOR if isEmpty(connector) else connector)
    elif code == CT_snake_case or code  == CT_SNAKE_CASE or code == CT_Snake_Case:
        _connector = (SNAKE_CONNECTOR if isEmpty(connector) else connector)

    _caseOp = getCaseOp(code)
    
    return _toCaseOp(str, _separators, _connector, _caseOp)

    # UNKNOWN CASE: use 'separators', 'connector'
    #_toCaseOp(str, separators, connector, CO_NONE)

# -  1. lowercase, [lower]~
# -  2. UPPERCASE, [upper]~
# -  3. camelCase, [camel]~
# -  4. CamelCase, PascalCase, [pascal]~
# -  5. snake_case, [snake]
# -  6. SNAKE_CASE, MACRO_CASE, CONSTANT_CASE, [SNAKE], [macro]~
# -  7. Snake_Case, [Snake]
# -  8. kebab-case, dash-case, train-case, lisp-case, [kebab]
# -  9. KEBAB-CASE, DASH-CASE, TRAIN-CASE, COBOL-CASE, [KEBAB], [cobol]~
# - 10. Kebab-Case, Dash-Case, Train-Case, HTTP-Header-Case, [Kebab], [http]~

# Return case code by case type
def getCaseCode(type):

    if type is None:
        return CT_NONE

    if type == 'lower':
        return CT_lowercase         # lowercase
    
    elif type == 'upper':
        return CT_UPPERCASE         # UPPERCASE

    elif type == 'camel':
        return CT_camelCase         # camelCase

    elif type == 'Camel' or type == 'Pascal' or type == 'pascal':
        return CT_PascalCase        # PascalCase

    elif type == 'snake':
        return CT_snake_case        # snake_case
    
    elif type == 'SNAKE' or type == 'MACRO' or type == 'macro':
        return CT_SNAKE_CASE        # SNAKE_CASE

    elif type == 'Snake':
        return CT_Snake_Case        # Snake_Case

    elif type == 'kebab' or type == 'dash' or type == 'train' or type == 'lisp':
        return CT_kebab_case        # kebab-case

    elif type == 'KEBAB' or type == 'DASH' or type == 'TRAIN' or type == 'COBOL' or type == 'cobol':
        return CT_KEBAB_CASE        # KEBAB-CASE

    elif type == 'Kebab' or type == 'Dash' or type == 'Train':
        return CT_Kebab_Case        # Kebab_Case

    return CT_NONE

# Return case op by case code
def getCaseOp(code):
    if code == CT_camelCase:
        # camelCase
        return CO_LOWER_CHAR # lower first char

    elif code == CT_PascalCase:
        # CamelCase
        return  CO_UPPER_CHAR # upper first char

    elif code == CT_kebab_case:
        # kebab-case
        return  CO_LOWER

    elif code == CT_KEBAB_CASE:
        # KEBAB-CASE
        return  CO_UPPER

    elif code == CT_Kebab_Case:
        # Kebab_Case
        return  CO_UPPER_CHAR

    elif code == CT_snake_case:
        # snake_case
        return  CO_LOWER

    elif code  == CT_SNAKE_CASE:
        # SNAKE_CASE
        return  CO_UPPER

    elif code  == CT_Snake_Case:
        # Snake_Case
        return  CO_UPPER_CHAR
    
    return CO_NONE
    
##################################################################

def reverse(str):
    if str is None:
        return None
    return str[::-1]

# 4.1

def startsWith(str, prefix):
    if isEmpty(str) or isEmpty(prefix):
        return False
    return str.startswith(prefix)

def endsWith(str, suffix):
    if isEmpty(str) or isEmpty(suffix):
        return False
    return str.endswith(suffix)

def startsWithIgnoreCase(str, prefix):
    if isEmpty(str) or isEmpty(prefix):
        return False
    strn = toIgnoreCase(str)
    prefixn = toIgnoreCase(prefix)
    return startsWith(strn, prefixn)

def endsWithIgnoreCase(str, suffix):
    if isEmpty(str) or isEmpty(suffix):
        return False
    strn = toIgnoreCase(str)
    suffixn = toIgnoreCase(suffix)
    return endsWith(strn, suffixn)

##

def hasPrefix(str, prefix):
    return startsWith(str, prefix)

def hasSuffix(str, suffix):
    return endsWith(str, suffix)

def hasPrefixIgnoreCase(str, prefix):
    return startsWithIgnoreCase(str, prefix)

def hasSuffixIgnoreCase(str, suffix):
    return endsWithIgnoreCase(str, suffix)

# 4.2

def removePrefix(str, prefix):
    if not hasPrefix(str, prefix):
        return str
    return str[len(prefix):]

def removePrefixes(str, prefixes):
    if isEmpty(str) or isEmpty(prefixes):
        return str    
    for prefix in prefixes:
        if isEmpty(prefix):
            continue
        if hasPrefix(str, prefix):
            return removePrefix(str, prefix)    
    return str

##

def removeSuffix(str, suffix):
    if not hasSuffix(str, suffix):
        return str
    return str[0:len(str)-len(suffix)]

def removeSuffixes(str, suffixes):
    if isEmpty(str) or isEmpty(suffixes):
        return str    
    for suffix in suffixes:
        if isEmpty(suffix):
            continue
        if hasSuffix(str, suffix):
            return removeSuffix(str, suffix)    
    return str

# 4.3

# internal
def _isQuoted(str, start, end):
    return startsWith(str, start) and endsWith(str, end) and size(str) >= size(start) + size(end)

def isQuoted(str, start = None, end = None):
    if isEmpty(str):
        return False
    
    # by default: '', ""    
    if start is None and end is None:
        return _isQuoted(str, '"', '"') or _isQuoted(str, "'", "'")
    
    if isEmpty(start) or isEmpty(end):
        return False # hard condition

    return _isQuoted(str, start, end)

def needQuote(str, start = None, end = None):
    return not isQuoted(str, start, end)

def quote(str, start = None, end = None):
    if str is None:
        return str # We can't quote None. But we can quote empty string
    
    # by default: ""
    if start is None and end is None:
        return '"' + str + '"'

    if isEmpty(start) or isEmpty(end):
        return str # hard condition

    return start + str + end

def unquote(str, start = None, end = None):
    if isEmpty(str):
        return str
    
    if start is None and end is None:
        if not isQuoted(str, None, None):
            return str
        else:
            return str[1:len(str)-1]

    if isEmpty(start) or isEmpty(end):
        return str # hard condition
    
    if not isQuoted(str, start, end):
        return str
    
    return str[len(start):len(str)-len(end)]

# 4.4

def isColumnSeparator(ch):
    if ch is None:
        return False
    return ch == '\r' or ch == '\n' or ch == '\t' # TODO: Use constant COLUMN_SEPARATORS = '\r\n\t'

def isColumnText(str, len = None):
    if isEmpty(str):
        return False
    
    if len is None:
        len = size(str)
    if len < 1:
        return False
    
    strLen = size(str) 
    if len >  strLen:
        len = strLen

    #Use pos
    #return findFirstOf(str, '\r\n\t') != -1 # TODO: Use constant COLUMN_SEPARATORS = '\r\n\t'
    
    i = 0
    while i < len:
        if isColumnSeparator(str[i]):
            return True
        i += 1
    return False

def isLineText(str, len = None):
    return not isColumnText(str, len)

# 5.1

def countChars(str, ch):
    if isEmpty(str) or isEmpty(ch):
        return 0
    
    if len(ch) != 1:
        return 0 # only one char, not string
    
    return str.count(ch)

    #len = size(str)
    #i = 0
    #count = 0
    #while i < len:
    #    if str[i] == ch:
    #        count += 1
    #    i += 1
    #return count

def countStrings(str, substr):
    if isEmpty(str) or isEmpty(substr):
        return 0
    
    return str.count(substr)
    
    #sublen = len(substr)
    #pos = 0
    #count = 0
    #while True:
    #    pos = findFirst(str, substr, pos)
    #    if pos == -1:
    #        break
    #    pos += sublen
    #    count += 1
    #return count

def countWords(str, separators = None):
    words = splitWords(str, separators) # TODO Optimize it
    return size(words)

def countLines(str):
    lines = splitLines(str)             # TODO Optimize it
    return size(lines)

# 6.1

# ObjLib: start ##########################

def isType(value, name):
    if value is None:
        return False
    return getTypeName(value) == name

def getTypeName(value):
    if value is None:
        return None
    return type(value).__name__

##

def isBoolType(value):
    return isType(value, 'bool')

def isIntType(value):
    return isType(value, 'int')

def isFloatType(value):
    return isType(value, 'float')

def isStrType(value):
    return isType(value, 'str')

def isListType(value):
    return isType(value, 'list')

def isDictType(value):
    return isType(value, 'dict')

# ObjLib: end ############################

def _replaceAll_str(str, s1, s2):
    return str.replace(s1, s2)

def _replaceAll_list(str, values1, values2):

    # [], []
    size1 = len(values1)
    size2 = len(values2)

    size = size1
    if size2 < size:
        size = size2

    if size == 0:
        return str
    
    value1 = None
    value2 = None
    result = str
    i = 0
    while i < size:
        value1 = values1[i]
        value2 = values2[i]
        i += 1

        if isEmpty(value1) or value2 is None:
            # ignore None/empty 'value1' or None 'value2'
            # empty 'value2' is correct case, we will remove 'value1' from 'str'
            continue

        if value1 == value2:
            # ignore this case because nothing to replace
            continue

        result = result.replace(value1, value2)
    return result

def _replaceAll_map(str, map):
    result = str
    for key, value in map.items():

        if isEmpty(key) or value is None:
            # ignore None/empty 'key' or None 'value'
            # empty 'value' is correct case, we will remove 'key' from 'str'
            continue

        if key == value:
            # ignore this case because nothing to replace
            continue

        result = result.replace(key, value)
    return result

def replaceAll(str, s1, s2 = None):
    if isEmpty(str):
        return str
    
    # dict    
    if s2 is None and isDictType(s1):
        return _replaceAll_map(str, s1)
    
    if isEmpty(s1) or s2 is None:
        # ignore None/empty 's1' or None 's2'
        # empty 's2' is correct case, we will remove 's1' from 'str'
        return str
    
    # str, str
    if isStrType(s1) and isStrType(s2):
        return _replaceAll_str(str, s1, s2)
    
    # list, list
    if isListType(s1) and isListType(s2):
        return _replaceAll_list(str, s1, s2)
    
    return str

# 7.1

# split

def split(str, separator = None, preserveAll = True):
    return splitBySeparator(str, separator, preserveAll)

def splitBySeparator(str, separator, preserveAll = True):
    return tokenizeBySeparator(str, separator, False, preserveAll)

def splitBySeparators(str, separators, preserveAll = True):
    return tokenizeBySeparators(str, separators, False, preserveAll)

# splitTrim

def splitTrim(str, separator = None, preserveAll = True):
    return splitTrimBySeparator(str, separator, preserveAll)

def splitTrimBySeparator(str, separator, preserveAll = True):
    elements = splitBySeparator(str, separator, preserveAll)
    trimElements(elements)
    return elements

def splitTrimBySeparators(str, separators, preserveAll = True):
    elements = splitBySeparators(str, separators, preserveAll)
    trimElements(elements)
    return elements

##

def splitWords(str, separators = None):
    if separators is None:
            separators = DEFAULT_WORD_SEPARATORS        
    return splitBySeparators(str, separators, False)


def splitLines(str):
    if isEmpty(str):
        return []
    return str.splitlines()

# tokenize

def _findFirst(mode, str, substr, pos):
    if mode == 1:
        # one separator
        return findFirst(str, substr, pos)
    else:
        # many separators
        return findFirstOf(str, substr, pos)

def _tokenize(mode, str, separator, includeAll = True, preserveAll = False):
    if isEmpty(str):
        return []
    
    #if isEmpty(separator):
    #    return [str]
    
    # Standard case: one separator (mode = 1)
    if mode == 1 and not includeAll and preserveAll:

        if separator is None:
            # Standard case
            return str.split()

        if len(separator) == 0:
            # 'split' doesn't support empty separator
            return [str]
        
        return str.split(separator)

    if separator is None:
        mode = 2
        separator = DEFAULT_SEPARATORS

        # Standard 'split' works with 'preserveAll = False' 
        # when separator is None 
        preserveAll = False 

    if isEmpty(separator):
        return [str]
    
    start = 0
    end = 0
    sep_len = 1

    if mode == 1:
        sep_len = len(separator) # real length of separator

    result = []

    while True:

        end = _findFirst(mode, str, separator, start)
        if end == -1:
            break

        if end - start == 0:
            if preserveAll and not includeAll:
                result.append('')
        else:
            result.append(str[start: end])         # end - start

        if includeAll:
            result.append(str[end: end + sep_len]) # sep_len

        start = end + sep_len

    if start == len(str):
        if preserveAll and not includeAll:
            result.append('')
    else:
        result.append(str[start:])

    return result

def tokenizeBySeparator(str, separator, includeAll = True, preserveAll = False):
    return _tokenize(1, str, separator, includeAll, preserveAll) # one separator

def tokenizeBySeparators(str, separators, includeAll = True, preserveAll = False):
    return _tokenize(2, str, separators, includeAll, preserveAll) # many seprators
