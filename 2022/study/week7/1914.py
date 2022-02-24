n = int(input())


def hanoi(n, f, e, t):  # t자리에 오면 보조기둥으로 사용
    if n == 1:
        print(f, e)
        return
    hanoi(n - 1, f, t, e)  # n-1 개의 원판을 f-> t로 이동
    print(f, e)  # 가장 큰 원판을 f->e로 이동
    hanoi(n - 1, t, e, f)  # n-1 개의 원판을 t -> e로 이동


if n <= 20:
    # 과정 출력
    print(pow(2, n) - 1)
    hanoi(n, 1, 3, 2)
else:
    # 과정 출력 x
    print(pow(2, n))
