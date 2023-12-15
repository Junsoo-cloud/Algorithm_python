array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복
        if array[j-1] > array[j]: # 한칸씩 왼쪽으로 이동
            array[j-1], array[j] = array[j], array[j-1] 
        else:
            break # 자기보다 작은 데이터 만나면 멈춤
print(array)

