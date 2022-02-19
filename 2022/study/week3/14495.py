# n = int(input())
# if n < 4:
#     print(1)
#     exit()
# else:
#     f = [0 for _ in range(117)]
#     f[1], f[2], f[3] = 1, 1, 1
#     for i in range(4, n + 1):
#         f[i] = f[i - 1] + f[i - 3]
#     print(f[n])
f = [0 for _ in range(117)]
f[1], f[2], f[3] = 1, 1, 1
n=int(input())
for i in range(4, n + 1):
    f[i] = f[i - 1] + f[i - 3]
print(f[n])
