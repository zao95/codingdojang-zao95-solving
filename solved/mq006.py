# 자작 문제풀이
# Question number. 006

# Author: Lee Jeongwoo
# Github name: zao95

# ========== Question ==========
# 숫자 암호화
# 입력받은 숫자를 암호화를 하는 코드를 작성하고,
# 그것을 복호화하는 코드를 작성하시오. 
# ==============================

def code_input():
    file_name = "code.txt"
    f = open(file_name, "w")
    f.write("Hello, World!")
    f.close()
    print("success code_input")

def encip():
    file_name = "code.txt"
    f =  open(file_name,"r")
    text_value = f.read()
    password = input("암호화에 사용할 %d 글자 비밀번호를 입력하세요." %(len(text_value)))
    f.close()
       
    changedcode = ""
    count = 0
    for i in text_value:
        codevalue = ord(i)
        print(i)
        print(ord(i))
        print("===")
        passwordvalue = ord(password[count])
        codevalue = codevalue + passwordvalue
        changed = chr(codevalue)
        changedcode = changedcode + changed
        count += 1
        print(codevalue)
        print("====")

    f2 = codecs.open("changed.txt", "w", "utf-8")
    f2.write(changedcode)
    f2.close()
    print("success encip")
    return changedcode


def decode():
    file_name = "changed.txt"
    f = codecs.open(file_name, "r", "utf-8")
    text_value = f.read()
    password = input("복호화에 사용할 %d 글자 비밀번호를 입력하세요." %(len(text_value)))
    f.close()
       
    changedcode = ""
    count = 0
    for i in text_value:
        codevalue = ord(i)
        print(i)
        print(ord(i))
        print("===")
        passwordvalue = ord(password[count])
        codevalue = codevalue - passwordvalue
        changed = chr(codevalue)
        changedcode = changedcode + changed
        count += 1

    f2 = codecs.open("recovered.txt", "w", "utf-8")
    f2.write(changedcode)
    f2.close()   
    return changedcode

if __name__ == "__main__":
    code_input()
    encip()
    decode()
