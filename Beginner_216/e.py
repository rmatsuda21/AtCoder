n, k = list(map(int, input().split(' ')))

at = sorted(list(map(int, input().split(' '))), reverse=True)

tot = 0

for _ in range(k):
    if at[0] == 0:
        break

    tot += at[0]
    at[0] -= 1

    if at[0] < at[1]:
        i = 1
        while i < n and at[1] == at[i]:
            i += 1
        
        tmp = at[0]
        at[0] = at[i-1]
        at[i-1] = tmp

print(tot)
