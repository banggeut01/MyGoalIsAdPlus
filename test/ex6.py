#ex6.py

'''
mkdir : 마지막 폴더만 읽어서 폴더 리스트에 추가해주기
rm : 삭제
cp 현재 + 뒤에 추가

'''

def solution(directory, command):
    answer = []
    dct = dict()
    for pwd in directory:
        dct[pwd] = True
    for li in command:
        co = list(li.split(" "))
        if co[0] == "mkdir":
            dct[co[1]] = True
        elif co[0] == "cp":
            tmp = []
            # co[1]로 시작하는 루트 검사
            for key in dct.keys():
                if key[:len(co[1])] == co[1]:
                    tmp.append(key)
            for key in tmp:
                dct[(co[2] + key).replace("//", "/")] = True

        else: # "rm"
            tmp = []
            # co[1]로 시작하는 루트 검사
            for key in dct.keys():
                if key[:len(co[1])] == co[1]:
                    tmp.append(key)
            for key in tmp:
                dct.pop(key)
    answer = sorted(list(dct))

    return answer
'''
directory = [
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
]
command = [
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]
'''
directory = [
"/"
]
command = [
"mkdir /a",
"mkdir /a/b",
"mkdir /a/b/c",
"cp /a/b /",
"rm /a/b/c"
]
print(solution(directory, command  ))