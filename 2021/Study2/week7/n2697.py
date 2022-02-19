t = int(input())
for _ in range(t):
    button = False
    arr = list(map(int, input()))
    answer = ''
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] <= arr[i - 1]:
            continue
        else:
            arr[i:] = sorted(arr[i:])
            for idx, num in enumerate(arr[i:]):
                if arr[i - 1] < num:
                    arr[i - 1], arr[idx + i] = arr[idx + i], arr[i - 1]
                    button = True
                    for a in range(len(arr)):
                        answer += str(arr[a])
                    print(answer)
                    break
            if button:
                break
    if not button:
        print("BIGGEST")
