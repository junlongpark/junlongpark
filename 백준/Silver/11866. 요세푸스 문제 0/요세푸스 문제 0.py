from collections import deque

def yos(n, k):
    col=deque(range(1, n+1))
    result=[]
    while col:
        for _ in range(k-1):
            col.append(col.popleft())
        result.append(col.popleft())
    return result

n, k = map(int, input().split())
sequence= yos(n,k)
print('<' + ', '.join(map(str,sequence))+'>')
