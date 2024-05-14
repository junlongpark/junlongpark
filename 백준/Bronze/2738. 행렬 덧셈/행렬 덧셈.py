A=[]
B=[]

N,M=map(int, input().split())
for r in range(N):
    a=list(map(int, input().split()))
    A.append(a)

for r in range(N):
    a=list((map(int, input().split())))
    B.append(a)

for r in range(N):
    for i in range(M):
        print(A[r][i]+B[r][i], end=" ")
    print()