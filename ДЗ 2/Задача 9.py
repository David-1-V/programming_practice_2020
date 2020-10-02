d={}
max=0
for _ in range (int(input())):
    for word in input().split ():
        if word in d:
            d[word]=d[word]+1
        else:
            d[word] = 1
        if d[word]>max:
            max=d[word]
for k,v in sorted (d.items()):
    if v==max:
        print (k)
        break