'''
이진트리
왼쪽 i*2, 부모 i, 오른쪽 자식 트리 i*2+1
9:58
'''

k = int(input())
array = [[] for _ in range(k)]  # idx 0은 데모 (무시하기)
input_array = list(map(int, input().split()))


def inorder(input_array, depth):
    # len이 1이 될때까지 계속 나눠줌
    if len(input_array) == 1:
        return
    mid = len(input_array) // 2
    array[depth].append(input_array[mid])
    inorder(input_array[:mid], depth + 1)  # 왼쪽 트리
    inorder(input_array[mid + 1:], depth + 1)  # 오른쪽 트리


inorder(input_array, 0)
for i in array:
    print(*i)
