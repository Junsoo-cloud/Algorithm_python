s = input()
res = ''
for x in s:
    if x.isdigit():
        res += x
print(int(res))
cnt = 0
for i in range(1, int(res)+1):
    if int(res)%i == 0:
        cnt += 1
print(cnt)