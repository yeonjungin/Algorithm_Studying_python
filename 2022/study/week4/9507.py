t = int(input())
array = [1, 1, 2, 4]
for i in range(4, 68):
    array.append(array[i - 1] + array[i - 2] + array[i - 3] + array[i - 4])
for i in range(t):
    n = int(input())
    print(array[n])

# t = int(input())
# array = [0 for _ in range(68)]
# array[0] = 1
# array[1] = 1
# array[2] = 2
# array[3] = 4
#
# for _ in range(t):
#     temp = int(input())
#     for n in range(4, temp + 1):
#         array[n] = array[n - 1] + array[n - 2] + array[n - 3] + array[n - 4]
#     print(array[temp])
