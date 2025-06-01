n = int(input())
number = list(map(int, input().split()))
M = max(number)
for i in range(n):
    number[i] = number[i]/M*100
print(sum(number)/n)