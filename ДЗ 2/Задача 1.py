n=[int(i) for i in input().split()]
s=0
for i in range (1, len(n)-1):
    if n[i-1]<n[i] and n[i]>n[i+1]:
        s=s+1
print (s)
