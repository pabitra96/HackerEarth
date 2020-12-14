num = [int(num) for num in input().split()]
l,r,k = num[0],num[1],num[2]
count=0
for i in range(l,r+1):
    if i%k == 0:
        count+=1
print(count)