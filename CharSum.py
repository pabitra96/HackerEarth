import sys
letter = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13,
          "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25,
          "z":26}
word = str(input())
leng = word.__len__()
if leng<1 and leng>100:
    sys.exit(0)
result = 0
for ele in word:
    result += letter[ele]
print(result)