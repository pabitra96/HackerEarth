import sys
string = str(input())
leng = string.__len__()
if leng<1 and leng>100:
    sys.exit(0)
revstr = (string[::-1])
if string == revstr:
    print("YES")
else:
    print("NO")