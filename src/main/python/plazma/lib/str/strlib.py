
EMPTY_STRING = ''
SPACE_CHAR = ' '
ELLIPSIS = '...'
ELLIPSIS_LEN = 3

DEFAULT_CASE_SEPARATOR = '_'
DEFAULT_CASE_SEPARATORS_ = ' -_'
DEFAULT_CASE_SEPARATORS_A = ' -_A'
DEFAULT_ALTER_CASE_SEPARATOR = '-' # XML    
DEFAULT_SNAKE_CASE_SEPARATOR = '_' # SNAKE
DEFAULT_KEBAB_CASE_SEPARATOR = '-' # KEBAB

####################################
# Case Operations
####################################
# caseOp =  1: 'myname': lowercase 
# caseOp =  2: 'MYNAME': UPPERCASE 
# caseOp =  3: 'myName': camelCase
# caseOp =  4: 'MyName': CamelCase
    
CO_NONE       =  0
CO_lowercase  =  1
CO_UPPERCASE  =  2
CO_camelCase  =  3
CO_PascalCase =  4

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

CT_lowercase  =  1
CT_UPPERCASE  =  2
CT_camelCase  =  3
CT_PascalCase =  4
CT_snake_case =  5
CT_SNAKE_CASE =  6
CT_Snake_Case =  7
CT_kebab_case =  8
CT_KEBAB_CASE =  9
CT_Kebab_Case = 10

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
# - noneIfEmpty(str, trim)                                     - trim, '' -> None
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

def noneIfEmpty(str, trim = False):
    if isEmpty(str):
        return None
    else:
        if trim:
            return str.strip() # trim
        else:
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
    if str is None:
        return None
    
    if n < 1:
        return str

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

def fill(str, len, pad = ' '):
    if str is None or len < 1:
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
    if str is None:
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
    if str is None:
        return None
        
    strLen = size(str)
    if strLen <= len:
        return str
    else:    
        return str[:len]

def right(str, len):
    if str is None:
        return None
        
    strLen = size(str)
    if strLen <= len:
        return str
    else:    
        return str[strLen - len:]

# 3.1

# - capitalize(str)
# - decapitalize(str

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
    
def capitalize(str, forceRest = False):
    if str is None:
        return None
    
    # return str.capitalize()
    # str[0:1].upper() + str[1:].lower()
    # return ''.join([str[:1].lower(), (str[1:].upper() if upper_rest else str[1:])])

    if len(str) == 0:
        return str

    # if 'forceRest' then lower rest
    return ''.join([str[0].upper(), (str[1:].lower() if forceRest else str[1:])])
    
def decapitalize(str, forceRest = False):
    if str is None:
        return None
        
    if len(str) == 0:
        return str

    # if 'forceRest' then upper rest
    return ''.join([str[0].lower(), (str[1:].upper() if forceRest else str[1:])])
    
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
def toCaseCode(type):

    if type is None:
        return None

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

    return 0

####

# Normalize Case Operation by Token position
def _normalizeCaseOpByToken(caseOp, first):
    _caseOp = caseOp
    if (caseOp == CO_camelCase):
        # camelCase: [0] -> 'lowercase', [1..n] -> 'PascalCase'
        _caseOp = (CO_lowercase if first else CO_PascalCase)    
    return _caseOp    

# caseOp =  1: 'myname': lowercase 
# caseOp =  2: 'MYNAME': UPPERCASE 
# caseOp =  3: 'myName': camelCase
# caseOp =  4: 'MyName': PascalCase
def _flushOp(result, buf, caseOp):
    caseOp = caseOp
    ch = 0
    str = ''

    for i in range(0, len(buf)):
        _caseOp = caseOp
        ch = buf[i]

        if caseOp == CO_PascalCase:
            if i == 0:
                _caseOp = CO_UPPERCASE  # upper char
            #else:
            #    _caseOp = CO_lowercase  # lower char

        # WARNING: We don't use 'caseOp' in this code because it is lower case always
        if _caseOp == CO_lowercase:
            ch = ch.lower()
        elif _caseOp == CO_UPPERCASE:
            ch = ch.upper()

        str = str + ch;                 # Add char to tring
        
    result.append(str);                 # Add buffer to result
    buf.clear();                        # Clear buffer

# splitOp: separators and A (Upper Char)
# caseOp =  1: 'myname': lowercase 
# caseOp =  2: 'MYNAME': UPPERCASE 
# caseOp =  3: 'myName': camelCase
# caseOp =  4: 'MyName': PascalCase
def _splitOp(str, separators, caseOp):
    result = []

    if isEmpty(str) or isEmpty(separators):
        result.append(str)
        return result

    strLen = len(str)
    sepLen = len(separators)

    ch = ''
    separator = ''
    find = False
    buf = []
    _caseOp = caseOp
    first = True
   
    for i in range(0, strLen):

        ch = str[i]
        find = False

        # Find a separator
        for j in range(0, sepLen):
            separator = separators[j]
            if separator == 'A': # TODO: 'A' is special marker for check 'Upper Char'
                if ch.isupper():
                    find = True
                    break
                    
            elif ch == separators[j]:
                find = True
                break

        if find:

            # flush
            if len(buf) > 0:
                _caseOp = _normalizeCaseOpByToken(caseOp, first)
                _flushOp(result, buf, _caseOp)
                first = False
                
            # Add separator: optional
            include = False
            if include or separator == 'A': # TODO: 'A' is special marker for check 'Upper Char'
                buf.append(ch)
                
        else:

            ## Add char
            buf.append(ch)

    # flush
    if len(buf) > 0:
        _caseOp = _normalizeCaseOpByToken(caseOp, first)
        _flushOp(result, buf, _caseOp)

    return result

# caseOp =  1: 'myname': lowercase 
# caseOp =  2: 'MYNAME': UPPERCASE 
# caseOp =  3: 'myName': camelCase
# caseOp =  4: 'MyName': PascalCase
def _toCaseOp(str, separators, connector, caseOp):
    if isBlank(str):
        return str
        
    result = '' 
    tokens = _splitOp(str, separators, caseOp)
    #print(tokens)
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

# caseOp =  1: 'myname': lowercase 
# caseOp =  2: 'MYNAME': UPPERCASE 
# caseOp =  3: 'myName': camelCase
# caseOp =  4: 'MyName': PascalCase
def _toTypeCase(str, type, separators, connector):

    if isEmpty(str):
        return str

    code = toCaseCode(type)
    if code <= 0:
        # Invalid case code
        return str        

    # SIMPLE CASE
    if code == CT_lowercase:
        return toCase(str, False) # lower case
    elif code == CT_UPPERCASE:
        return toCase(str, True)  # UPPER case

    # COMPLEX CASE
    _separators = (DEFAULT_CASE_SEPARATORS_A if isEmpty(separators) else separators)

    if code == CT_camelCase:
        # camelCase
        return _toCaseOp(str, _separators, connector, CO_camelCase); # lower first char

    elif code == CT_PascalCase:
        # CamelCase
        return _toCaseOp(str, _separators, connector, CO_PascalCase); # upper first char

    elif code == CT_kebab_case:
        # kebab-case
        return _toCaseOp(str, _separators, (KEBAB_CONNECTOR if isEmpty(connector) else connector), CO_lowercase)

    elif code == CT_KEBAB_CASE:
        # KEBAB-CASE
        return _toCaseOp(str, _separators, (KEBAB_CONNECTOR if isEmpty(connector) else connector), CO_UPPERCASE)

    elif code == CT_Kebab_Case:
        # Kebab_Case
        return _toCaseOp(str, _separators, (KEBAB_CONNECTOR if isEmpty(connector) else connector), CO_PascalCase)

    elif code == CT_snake_case:
        # snake_case
        return _toCaseOp(str, _separators, (SNAKE_CONNECTOR if isEmpty(connector) else connector), CO_lowercase)

    elif code  == CT_SNAKE_CASE:
        # SNAKE_CASE
        return _toCaseOp(str, _separators, (SNAKE_CONNECTOR if isEmpty(connector) else connector), CO_UPPERCASE)

    elif code  == CT_Snake_Case:
        # Snake_Case
        return _toCaseOp(str, _separators, (SNAKE_CONNECTOR if isEmpty(connector) else connector), CO_PascalCase)

    # UNKNOWN CASE: use 'separators', 'connector'
    #_toCaseOp(str, separators, connector, CO_NONE)

def toCamelCase(str, separators = None, capitalize = True):
    if isEmpty(str):
        return str

    type = 'Camel' if capitalize else 'camel'
    return _toTypeCase(str, type, separators, None)

def toSnakeCase(str, separators = None, upper = True):
    if isEmpty(str):
        return str

    type = 'SNAKE' if upper else 'snake'
    return _toTypeCase(str, type, separators, '_')

def toKebabCase(str, separators = None, upper = True):
    if isEmpty(str):
        return str

    type = 'KEBAB' if upper else 'kebab'
    return _toTypeCase(str, type, separators, '-')
