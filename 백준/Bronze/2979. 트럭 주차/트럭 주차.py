a, b, c = map(int, input().split())
time_count = []
time_count = [0] * 101  # 1~100시간 동안 각 시간에 트럭 수를 저장


for i in range(3):
    start, end = map(int, input().split())
    for j in range(start, end):
        time_count[j] += 1

total=0
for i in range(1, 101):
    time = time_count[i]
    if time == 1:
        total += 1*a
    if time == 2:
        total += 2*b
    if time == 3:
        total += 3*c
print(total)