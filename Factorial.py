import sys
n=int(input())
if n<1 or n>10:
    sys.exit(0)
x = 1
while n>1:
    x*=n
    n-=1
print(x)