n = int(input())

ans = ''

while n > 0:
    if n%2 == 1:
        n -= 1
        ans += 'A'
    else:
        n //= 2
        ans += 'B'

print(ans[::-1])