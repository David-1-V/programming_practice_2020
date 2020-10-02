n=[int(i) for i in input().split()]
s=0
for i in range (len(n)):
    k=0
    while k+i+1<len(n):
        if n[i]==n[k+i+1]:
            s=s+1
        k=k+1
print(s)