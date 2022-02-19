'''x=int(input())
array=[64]
while sum(array)>x: # 합>x
        # 1번
        min_value=min(array) # 가장 짧은 막대를 절반으로 나눈다.
        array.remove(min_value)
        array.append(min_value//2)
        array.append(min_value//2)
        array=sorted(array)
        if sum(array)-min_value//2 >=x:
            array.remove(min_value//2)
            continue
print(len(array))'''
print(sum(list(map(int, bin(int(input()))[2:]))))