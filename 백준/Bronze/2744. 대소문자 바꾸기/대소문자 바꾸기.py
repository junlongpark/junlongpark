for i in input():
    if i.isupper():    #문자열이 대문자인지 true or false로 반환
        print(i.lower(), end='') #소문자로 변환
    else:
        print(i.upper(), end='')