# 자작 문제풀이
# Question number. 004

# Author: Lee Jeongwoo
# Github name: zao95

# ========== Question ==========
# 철수는 현재 아래 지도에서 좌상단에 위치하고 있다.
# 철수는 지금부터 우하단에 위치한 집을 향해 가는데,
# 최단거리로 가는 전제하에 가는 길의 숫자와 연산자로 계산하면서 간다면,
# 최소값과 최대값은 얼마이고, 그 길은 어떤 길인가?
# route_map = [
#     ['1', '-', '2', '-', '5', ],
#     ['-', '4', '*', '8', '*', ],
#     ['6', '+', '3', '-', '2', ],
#     ['*', '4', '*', '8', '+', ],
#     ['9', '+', '5', '+', '8', ],
# ]
# ==============================

# import
import random
from modules import mq004_module

route_map = [
    [1, '-', 2, '-', 5, ],
    ['+', 4, '*', 8, '*', ],
    [6, '+', 3, '-', 2, ],
    ['*', 4, '*', 8, '+', ],
    [9, '+', 5, '+', 8, ],
]
move_sequence = [[True, True, True, True], [False, False, False, False]]
move_count = 0
res = []

if __name__ == '__main__':

    for i in range(0, 5, 1):
        for j in range(0, len(move_sequence[0])):
            for k in range(0, len(move_sequence[1])):
                res.append(mq004_module.move(route_map, mq004_module.route_change(move_sequence, move_count, j, k)))
                print("최소값 : " + str(min(res)))
                print("최대값 : " + str(max(res)))
                move_count += 1

# ===== 참조 =====
# # 경우의 수
# # 팩토리얼에서 *이 +가 된 형태
# a = (
#     (1)+
#     (2+1)+(1)+
#     (3+2+1)+(2+1)+(1)+
#     (4+3+2+1)+(3+2+1)+(2+1)+1+
#     ((4+3+2+1)+(3+2+1)+(2+1)+1)+((3+2+1)+(2+1)+1)+((2+1)+1)+1
# )
# print(a)

# 1     1
# 5     4
# 15    10
# 35    20
# 70    35