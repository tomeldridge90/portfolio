'''
<<<<<Question>>>>>

Write a function that accepts a string consisting only of ASCII letters and the whitespace
and returns that string in block letters of 5 characters width and 7 characters height, with
one space between characters.

- The block letters should consist of corresponding capital letters.

- It's irrelevant whether input consists of lower or upper case letters.

- Any leading and/or trailing whitespaces in input should be ignored.

- Empty strings or such containing only whitespaces should return an empty string.

- The remaining spaces (between letters and/or words) are to be treated as any other character.
  This means that there will be six spaces in output for a space in input, or a multiple of six,
  if there were more spaces - plus the one from preceding character!

- Trailing spaces should be removed in the resulting string.

- The string should be formatted in a way that when passed to your languages built-in print()/puts
  function shows the desired output (see below for example).

  "block_print('heLLo WorLD')"

  will result in a string that looks like this when passed to e. g. pythons print() function:

H   H EEEEE L     L      OOO        W   W  OOO  RRRR  L     DDDD
H   H E     L     L     O   O       W   W O   O R   R L     D   D
H   H E     L     L     O   O       W   W O   O R   R L     D   D
HHHHH EEEEE L     L     O   O       W W W O   O RRRR  L     D   D
H   H E     L     L     O   O       W W W O   O R R   L     D   D
H   H E     L     L     O   O       W W W O   O R  R  L     D   D
H   H EEEEE LLLLL LLLLL  OOO         W W   OOO  R   R LLLLL DDDD

'''

'''
<<<<<Answer>>>>>
'''
letters =  {'A':[' AAA ','A   A','A   A','AAAAA','A   A','A   A','A   A'],
            'B':['BBBB ','B   B','B   B','BBBB ','B   B','B   B','BBBB '],
            'C':[' CCC ','C   C','C    ','C    ','C    ','C   C',' CCC '],
            'D':['DDDD ','D   D','D   D','D   D','D   D','D   D','DDDD '],
            'E':['EEEEE','E    ','E    ','EEEEE','E    ','E    ','EEEEE'],
            'F':['FFFFF','F    ','F    ','FFFFF','F    ','F    ','F    '],
            'G':[' GGG ','G   G','G    ','G GGG','G   G','G   G',' GGG '],
            'H':['H   H','H   H','H   H','HHHHH','H   H','H   H','H   H'],
            'I':['IIIII','  I  ','  I  ','  I  ','  I  ','  I  ','IIIII'],
            'J':['JJJJJ','    J','    J','    J','    J','    J','JJJJ '],
            'K':['K   K','K  K ','K K  ','KK   ','K K  ','K  K ','K   K'],
            'L':['L    ','L    ','L    ','L    ','L    ','L    ','LLLLL'],
            'M':['M   M','MM MM','M M M','M   M','M   M','M   M','M   M'],
            'N':['N   N','NN  N','N   N','N N N','N   N','N  NN','N   N'],
            'O':[' OOO ','O   O','O   O','O   O','O   O','O   O',' OOO '],
            'P':['PPPP ','P   P','P   P','PPPP ','P    ','P    ','P    '],
            'Q':[' QQQ ','Q   Q','Q   Q','Q   Q','Q Q Q','Q  QQ',' QQQQ'],
            'R':['RRRR ','R   R','R   R','RRRR ','R R  ','R  R ','R   R'],
            'S':[' SSS ','S   S','S    ',' SSS ','    S','S   S',' SSS '],
            'T':['TTTTT','  T  ','  T  ','  T  ','  T  ','  T  ','  T  '],
            'U':['U   U','U   U','U   U','U   U','U   U','U   U',' UUU '],
            'V':['V   V','V   V','V   V','V   V','V   V',' V V ','  V  '],
            'W':['W   W','W   W','W   W','W W W','W W W','W W W',' W W '],
            'X':['X   X','X   X',' X X ','  X  ',' X X ','X   X','X   X'],
            'Y':['Y   Y','Y   Y',' Y Y ','  Y  ','  Y  ','  Y  ','  Y  '],
            'Z':['ZZZZZ','    Z','   Z ','  Z  ',' Z   ','Z    ','ZZZZZ'],
            ' ':['     ','     ','     ','     ','     ','     ','     ']
            }

def block_print(string):
    capitalString = string.upper().strip()
    count=0
    returnString = ''
    while count<7:
        if count !=0:
            returnString += '\n'
        for letter in capitalString:
            returnString += (letters[letter][count] +' ')
        count+=1
        returnString = returnString.rstrip()
    return returnString

print(block_print('heLLo WorLD'))

