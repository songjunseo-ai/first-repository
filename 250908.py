print("잠 하루종일 자고싶다")
print("헬스장 가고싶다")
print("집가고싶다")
dict1 = {"홍길동":100, "이순신": 55}

print(dict1["홍길동"]) # 값 출력
print(dict1.values()) # 값만 모아 리스트로 출력
print(dict1.keys()) # 키만 모아 리스트로 출력

dict1.pop("이순신") #삭제
del dict1["홍길동"] #삭제

dict1["홍길동"] = 100 #추가
dict1["이순신"] = 95

if "강감찬" not in dict1:
    dict1["강감찬"] = 80 # 없으면 추가

for key in dict1:
    print(key) # 키만 모아서 출력

print(dict1)

dict2 = {x: x**2 for x in range(1,21) if x%3==0 } #리스트 축약
print(dict2)