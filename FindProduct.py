from array import*
n = int(input())
num = [int(num) for num in input().split()]
out = 1
k=0
for j in num:
    out*= j
    out = out % (10**9 + 7)
    k+=1
print(out)