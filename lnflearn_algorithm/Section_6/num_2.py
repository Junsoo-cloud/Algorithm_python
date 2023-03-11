'''Num_2: Preorder, Inorder, Postorder travelsal'''
# Preorder_travalsal
# Stack
# Recursion
def DFS(n):
    if n > 7:
        return
    else:
        print(n, end = ' ')
        DFS(2*n) # left node
        DFS(2*n+1) # right node
if __name__ == '__main__':
    DFS(1)
