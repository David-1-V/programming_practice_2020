n=[int(k) for k in input().split()]
index_min=0
index_max=0
for i in range (1, len(n)):
    if n[i]>n[index_max]:
        index_max=i
    if n[i] < n[index_min]:
        index_min = i
n[index_min], n[index_max]=n[index_max],n[index_min]
print (' '.join([str(i) for i in n]))
