n = int(input())

firstNames = {}

ans = 'No'
for i in range(n):
    (f, l) = input().split(' ')
    if f in firstNames:
        if l in firstNames[f]:
            ans = 'Yes'
            break
        else:
            firstNames[f].append(l)
    else:
        firstNames[f] = [l]

print(ans)