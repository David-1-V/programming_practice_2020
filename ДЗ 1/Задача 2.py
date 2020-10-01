n=int(input())
t=str(input())
s='Hello,'
for i in range (n):
    s+=(' '+t+',')
print (s[0:-1])