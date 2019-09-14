# 코딩도장 문제풀이
# 사이냅소프트 면접문제
# http://codingdojang.com/scode/410

# Author: Lee Jeongwoo
# Github name: zao95

# ========== Question ==========
# 주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.
# 이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

# 김씨와 이씨는 각각 몇 명 인가요?
# "이재영"이란 이름이 몇 번 반복되나요?
# 중복을 제거한 이름을 출력하세요.
# 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
# ==============================

input_data = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
input_data_list = input_data.split(",")

# 1
ans1_1 = len([x for x in input_data_list if x[0] == "김" or x[0] == "이"])
ans1_2 = len([x for x in input_data_list if x[0] == "김" or x[0] == "이"])
ans1 = '김씨: {kim}명, 이씨: {lee}명'.format(kim=ans1_1, lee=ans1_2)

print(ans1)

# 2
ans2 = len([x for x in input_data_list if x == "이재영"])

print(input_data_list.count("이재영"))

print(ans2)

# 3
ans3 = list(set(input_data_list))

ans3 = list(set(input_data_list))

print(ans3)

# 4
ans4 = sorted(ans3)
print(ans4)