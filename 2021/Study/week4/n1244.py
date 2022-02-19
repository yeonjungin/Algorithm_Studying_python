switch_num = int(input())
array = list(map(int, input().split()))  # turn on 1 , turn off 0
student = int(input())


def man(array, num):
    for i in range(1, switch_num // num + 1):
        idx = num * i - 1
        array[idx] = int(not array[idx])
    return array


def woman(array, num):
    mid = num - 1
    left = mid - 1
    right = mid + 1
    array[mid] = int(not array[mid])  # 현재 스위치 상태 바꾸기
    while True:
        if left >= 0 and right < len(array):  # 구간내에 있으면
            if array[left] == array[right]:  # 대칭이면
                array[left] = int(not array[left])
                array[right] = int(not array[right])
                left-=1
                right+=1
                continue
            # 대칭아니면?
            return array
        else:
            return array


for i in range(student):
    gender, num = map(int, input().split())
    if gender == 1:  # 남
        man(array, num)
        continue
    # 여
    woman(array, num)

for i in range(1,switch_num+1):
    if i%20==0: #줄바꿈
        print(array[i-1])
    else:
        print(array[i-1],end=' ')
