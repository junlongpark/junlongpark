a=list(range(1,31))
for i in range(28):
    b=int(input())
    a.remove(b)
print(min(a))
print(max(a))