from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
card_count = Counter(cards)  # 카드별 개수를 딕셔너리 형태로 저장

m = int(input())
targets = list(map(int, input().split()))

for num in targets:
    print(card_count[num], end=' ')

