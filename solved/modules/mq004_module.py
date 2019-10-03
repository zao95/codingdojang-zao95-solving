# import
import copy


def route_change(sequence_data, count, i, j):
    # 가는 길을 바꿔주는 부분
    sequence = copy.deepcopy(sequence_data)
    print(str(count) + " 번째 출발")
    if count == 0:
        pass

    sequence[0][i] = not sequence[0][i]
    sequence[1][j] = not sequence[1][j]
    print("출발 시퀸스 : " + str(sequence))
    return sequence
    

def move(route_map_data, sequence):
    x = 0
    y = 0
    route = [route_map_data[y][x]]
    temp = []

    # 이동하는 부분
    for i in sequence[0] + sequence[1]:
        if i:
            x += 1
        else:
            y += 1
        route.append(route_map_data[y][x])

    # 연산 함수
    def calc(oper):
        position = route.index(oper)
        if oper == '+':
            route[position-1] = route[position-1] + route[position+1]
        if oper == '-':
            route[position-1] = route[position-1] - route[position+1]
        if oper == '*':
            route[position-1] = route[position-1] * route[position+1]
        del route[position]
        del route[position]

    # 연산하는 부분
    while route.count('*'): # 곱연산 우선
        calc('*')
    while route.count('+') or route.count('-'):
        if route.count('+'):
            calc('+')
        elif route.count('-'):
            calc('-')
    print("결과 : " + str(route))
    return route

if __name__ == "__main__":
    # route_change([[True, True, True, True], [False, False, False, False]], 0, 0, 0)
    move(
        [
            [1, '-', 2, '-', 5, ],
            ['+', 4, '*', 8, '*', ],
            [6, '+', 3, '-', 2, ],
            ['*', 4, '*', 8, '+', ],
            [9, '+', 5, '+', 8, ],
        ], 
        [[True, True, True, True], [False, False, False, False]]
    )