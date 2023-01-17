# symbols = '$¢£¥€¤'

# beyond_ascii = [ord(s) for s in symbols if ord > 127]

symbols = '$¢£¥€¤'

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

print(beyond_ascii)

nombre = "dario"

nombre2 = list(map(lambda x: x.upper(), nombre))

print(nombre2)