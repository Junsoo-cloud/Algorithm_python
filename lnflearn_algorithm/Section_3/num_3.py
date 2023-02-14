'''Num_3'''
cards = list(range(1,21))
for _ in range(0, 10):
    ai, bi = map(int, input().split())
    for j in range(bi - ai + 1):
        while ai < bi:
            cards[ai-1], cards[bi-1] = cards[bi-1], cards[ai-1]
            ai += 1
            bi -= 1
print(cards)    
