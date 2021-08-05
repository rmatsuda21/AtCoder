n = int(input())
nums = sorted(list(map(int,input().split(' '))))

tot = 1
for i in range(len(nums)):
    tot *= nums[i] - i
    tot %= 1000000007

print(tot)