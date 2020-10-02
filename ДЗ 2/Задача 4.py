n=[int(h) for h in input().split()]
for i in range (len(n)):
    for y in range (len(n)):
        if i!=y and n[i]==n[y]:
            break
    else:
        print(n[i])
