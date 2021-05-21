input_num = int(input())
map_size = input_num * 4 - 3
star_map = [[' '] * map_size for _ in range(map_size)]


def draw(input_num, idx):
    if input_num == 1:
        star_map[idx][idx] = '*'
        return

    l = 4 * input_num - 3
    for i in range(idx, l + idx):
        star_map[idx][i] = "*"
        star_map[idx + l - 1][i] = "*"

        star_map[i][idx] = "*"
        star_map[i][idx + l - 1] = "*"
    return draw(input_num - 1, idx + 2)

draw(input_num, 0)

for i in range(map_size):
    for j in range(map_size):
        print(star_map[i][j],end='')
    print()