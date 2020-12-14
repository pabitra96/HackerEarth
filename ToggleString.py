word=input()
newword=""
for i in word:
    if(i.islower())==True:
        newword+=i.upper()
    elif(i.isupper())==True:
        newword+=i.lower()
print(newword)