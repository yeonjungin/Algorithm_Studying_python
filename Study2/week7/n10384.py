t = int(input())

for k in range(1, t + 1):
    word = input()
    array = [0 for _ in range(26)]
    for i in word:
        if i >= 'a' and i <= 'z':
            idx = ord(i) - ord('a')  # a : 97 , A : 65
            array[idx] += 1
        if i >= 'A' and i <= 'Z':
            idx = ord(i) - ord('A')
            array[idx] += 1
    answer = 3
    for i in array:
        answer = min(answer, i)

    if answer == 0:
        print("Case {}: Not a pangram".format(k))
    elif answer == 1:
        print("Case {}: Pangram!".format(k))
    elif answer == 2:
        print("Case {}: Double pangram!!".format(k))
    else:
        print("Case {}: Triple pangram!!!".format(k))
