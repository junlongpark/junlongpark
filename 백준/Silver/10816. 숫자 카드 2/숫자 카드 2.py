import sys
input = sys.stdin.readline
from collections import Counter
n=int(input())

cards = list(map(int, input().split()))
cards_count = Counter(cards)

m=int(input())
target = list(map(int, input().split()))

for num in target:
    print(cards_count[num], end=' ')
