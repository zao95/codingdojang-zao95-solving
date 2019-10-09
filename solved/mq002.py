# 자작 문제풀이
# Question number. 002

# Author: Lee Jeongwoo
# Github name: zao95

# ========== Question ==========
# 아래에 적힌 정렬방식을 난수 100개가 담긴 리스트에 대해 모두 구현하시오.

# 순차 정렬, 버블 정렬, 선택 정렬, 삽입 정렬, 쉘 정렬, 퀵 정렬, 병합 정렬, 힙 정렬
# ==============================

# import
import random
from modules import mq002_module

# create random list
random_list = []
for i in range(0, 1000):
    random_list.append(random.randint(1, 100))

test1 = mq002_module.Sort()
test1.setting(random_list)
test1.sequential_1()
test1.bubble_1()
test1.selection_1()
test1.insertion_1()
test1.insertion_2()