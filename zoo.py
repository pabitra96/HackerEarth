import sys
fullstr = input()
countz = 0
counto = 0
if len(fullstr) < 21:
    for i in fullstr:
        if i == 'z':
            countz+=1
        if i == 'o':
            counto+=1
    if counto == 2*countz:
        print("Yes")
    else:
        print("No")
else:
    sys.exit()