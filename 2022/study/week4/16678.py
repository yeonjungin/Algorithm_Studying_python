n = int(input())
array = sorted(list(int(input()) for _ in range(n)))
answer = 0
t=1
for num in range(n):
    # array = [array[i] - 1 for i in range(n)]
    if array[num] >= t:
        answer += array[num]-t
        t+=1
print(answer)

# now=1
# for num in array:
#     if num>=now:
#         answer+=num-now
#         now+=1
# print(answer)
