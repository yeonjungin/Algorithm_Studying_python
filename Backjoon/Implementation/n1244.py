# 1244번. 스위치 켜고 끄기
switch_num = int(input())
state = list(map(int, input().split()))
student_num = int(input())

def man(array, num):
    for i in range(switch_num // num):
        idx = ((i + 1) * num) - 1
        array[idx] = int(not array[idx])
    return array

def woman(array, num):
    center = num - 1
    idx = 1
    array[center] = int(not array[center])

    while True:
        if center - idx > -1 and center + idx < switch_num:
            if array[center - idx] == array[center + idx]:
                array[center - idx] = int(not array[center - idx])
                array[center + idx] = int(not array[center + idx])
                idx += 1
                continue
            else:
                return array
        else:
            return array

for i in range(student_num):
    array = list(map(int, input().split()))
    if array[0] == 1:
        man(state, array[1])
        continue
    else:
        woman(state, array[1])

for i in range(1, switch_num + 1):
    if i % 20 == 0:
        print(state[i - 1])
    else:
        print(state[i - 1], end=' ')
