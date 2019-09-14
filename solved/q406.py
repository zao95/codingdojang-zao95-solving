# 코딩도장 문제풀이
# Question number. 406
# 게시판 페이징
# http://codingdojang.com/scode/406

# Author: Lee Jeongwoo
# Github name: zao95

# ========== Question ==========
# A씨는 게시판 프로그램을 작성하고 있다.
# A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.

# 입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)
# 출력 : 총페이지수

# A씨가 필요한 프로그램을 작성하시오.
# ==============================

import math

m = int(input('총건수: '))
n = int(input('한페이지에 보여줄 게시물수: '))

ans = math.ceil(m/n)
print(ans)