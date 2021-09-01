s = list(map(int, input().split('.')))

if 0 <= s[1] <= 2:
    print(str(s[0])+'-')
elif 3 <= s[1] <= 6:
    print(s[0])
elif 7 <= s[1] <= 9:
    print(str(s[0])+'+')
