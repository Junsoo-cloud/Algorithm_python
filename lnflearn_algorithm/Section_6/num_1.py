'''Nu_1: 재귀함수를 이용한 이진수 출력(Recursion)'''
import sys
sys.stdin=open('input.txt', 'r')
n = int(input())
def DFS(n):
    if n == 0:
        return
    else:
        DFS(n//2)
        print(n%2, end = ' ')
if __name__ == '__main__':
    DFS(n)
    
# Recursion & Stack 이해를 잘해야 함 !!