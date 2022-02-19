answer_num = 0
answer = ''


def permu(n, cnt):
    global answer_num
    global answer
    if len(answer) == len(word):
        answer_num += 1
        if answer_num == n:
            return False

    for j in range(0, len(word)):
        if visited[j]:
            continue

        visited[j] = 1
        answer += word[j]
        permu(n, cnt + 1)
        if answer_num == n:
            return False
        visited[j] = 0
        answer = answer[:-1]

    return True


while True:
    try:
        word, n = input().split()
        n = int(n)
        cnt = 0
        if n == '':
            break
        visited = [0 for _ in range(len(word))]
        answer = ''
        answer_num = 0
        button = False
        for idx in range(0, len(word)):
            visited[idx] = 1
            answer = word[idx]
            if not permu(n, cnt + 1):
                print('{} {} = {}'.format(word, n, answer))
                button = True
                break
            visited[idx] = 0
        if not button:
            print('{} {} = No permutation'.format(word, n))


    except EOFError:
        break
