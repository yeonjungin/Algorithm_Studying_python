n = int(input())
pattern = input().split("*")

for _ in range(n):
    temp = input()
    if temp[:len(pattern[0])]==pattern[0] and temp[-len(pattern[1]):]==pattern[1] and len(temp)>=len("".join(pattern)):
        print("DA")
    else:
        print("NE")
