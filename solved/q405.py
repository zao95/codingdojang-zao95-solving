# 코딩도장 문제풀이
# Question number. 405
# 탭을 공백 문자로 바꾸기
# http://codingdojang.com/scode/405

# Author: Lee Jeongwoo
# Github name: zao95

# ========== Question ==========
# A씨는 개발된 소스코드를 특정업체에 납품하려고 한다. 
# 개발된 소스코드들은 탭으로 들여쓰기가 된것, 공백으로 들여쓰기가 된 것들이 섞여 있다고 한다. 
# A씨는 탭으로 들여쓰기가 된 모든 소스를 공백 4개로 수정한 후 납품할 예정이다.
# A씨를 도와줄 수 있도록 소스코드내에 사용된 탭(Tab) 문자를 공백 4개(4 space)로 바꾸어 주는 프로그램을 작성하시오.
# ==============================
from pathlib import Path

# path import
path = Path("solved/files/f405.txt")
# change to the absolute path
full_path = path.absolute()
# change to string type
my_path = full_path.as_posix()

with open(my_path,'r') as f:
    data = f.read()
    with open(my_path[:-3]+'ans.txt', 'w') as write_data:
        write_data.write(data.replace('\t', '    '))