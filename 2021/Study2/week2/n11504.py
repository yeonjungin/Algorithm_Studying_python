t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    ex = input().split()
    x = int(''.join([i for i in ex]))

    ey = input().split()
    y = int(''.join([i for i in ey]))

    array = input().split()
    new_array = array + array[:m - 1]
    result = 0

    for k in range(int(ex[0]), int(ey[0]) + 1):
        idx = [i for i, value in enumerate(array) if int(value) == k]
        for j in idx:
            now = int(''.join(new_array[j:j + m]))
            if x <= now <= y:
                result += 1
    print(result)
