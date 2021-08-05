(n, x) = map(int, input().split(' '))

prices = list(map(int, input().split(' ')))

tot = 0
for i in range(len(prices)):
    if (i+1)%2 == 0:
        tot += prices[i] - 1
    else:
        tot += prices[i]

if tot > x:
    print('No')
else:
    print('Yes')