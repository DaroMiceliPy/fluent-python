symbols = '$¢£¥€¤'

print(tuple(ord(symbol) for symbol in symbols)) #No need to enclose parentheses

import array
print(array.array("I", (ord(symbol) for symbol in symbols))) #We need to enclose with parentheses because there are two arguments


