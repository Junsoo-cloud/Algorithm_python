# minimum
'''Num_4'''
n = int(input())
arrmin = 2147000000
scores = list(map(int, input().split()))
all_scores = sum(scores)
aver_score = round(all_scores / n)
for idx, x in enumerate(scores):
    tmp = abs(aver_score - x)
    if tmp < arrmin:
        arrmin = tmp
        score = x
        res = idx + 1
    elif tmp == arrmin:
        if x > score: # 같은건 그냥 넘어감
            score = x
            res = idx + 1
# 최솟값을 for 루프로, + enumerate까지 잘 활용해야 했음