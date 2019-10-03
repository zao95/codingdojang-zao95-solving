# 자작 문제풀이
# Question number. 001

# Author: Lee Jeongwoo
# Github name: zao95

# ========== Question ==========
# 임의의 자연수 2개에 대한 최소공약수와 최대공약수를 구하라
# ==============================

num1 = 8
num2 = 12

ans1 = max([x for x in range(1, max(num1, num2)) if num1 % x == 0 and num2 % x == 0])
ans2 = int((num1 * num2) / ans1)

print("최대공약수: {ans}".format(ans = ans1))
print("최소공배수: {ans}".format(ans = ans2)) 