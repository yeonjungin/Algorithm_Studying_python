#1
import sys
for i in sys.stdin:
    temp="-"
    for j in range(int(i)):
        temp=temp+" "*len(temp)+temp
    print(temp)

#2
# def recursive(array, start, now_length):
#     temp = now_length // 3
#
#     if temp == 0:
#         return
#
#     for i in range(start + temp, start + temp * 2):
#         array[i] = ' '
#
#     recursive(array, start, temp)
#     recursive(array, start + temp * 2, temp)
#
#
# while True:
#     try:
#         n = input()
#         if n == '':
#             break
#         else:
#             n = int(n)
#             array = ['-' for i in range(pow(3, n))]
#             recursive(array, 0, pow(3, n))
#             answer = ''
#             for i in array:
#                 answer += i
#             print(answer)
#
#     except EOFError:
#         break
#
# # 입력 도중에 파일의 끝을 만나면 반복문 종료


