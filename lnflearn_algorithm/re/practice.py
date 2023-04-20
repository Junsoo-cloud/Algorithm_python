import sys
sys.stdin=open('input.txt', 'r')
s = input()
tot = 0
res = ''
for x in s:
    if x.isdigit():
        tot += int(x) 
    else:
        res += x
res = sorted(res)
res += str(tot)
print(''.join(res))