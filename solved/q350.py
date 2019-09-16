# 코딩도장 문제풀이
# Question number. 350
# Multiples of 3 and 5
# http://codingdojang.com/scode/350

# Author: Lee Jeongwoo
# Github name: zao95

# ========== Question ==========
# [문제]
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# [번역]
# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.
# ==============================

ans = sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0])
print(ans)