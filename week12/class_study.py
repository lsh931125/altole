# 클래스

# 중괄호 가지고 감싸져있어서 키와 밸류값이 쌍으로 이루어져 있는 형태
# 딕셔너리
# 객체(Object)라고 볼 수있다. - 파이썬 뿐 아니라 클래스를 지원하는 모든 언어에서 아래와 같은 형태를 이용한다.

# 밑에는 예시 객체라고 보았을때, 파이써는 딕셔너리라고 인식함.
# memberInfo = {
#     "name" : "짱구", # 프로퍼티(property) - 객체 안에있는 일반 값을 프로퍼티라고 함.
#     "age" : 5,
#     "sayHi" : def () { # 메소드(method) - 객체안에있는 함수를 메소드라고 함.
#         print("Hi")
#     }
# }

# 객체에 접근하고 싶다면 변수명.키값 - 클래스가 생성

class Member:
    def __init__(self, name, age):
        # 기본 프로퍼티값 생성
        self.name = name
        self.age = age

    def sayHi(self):
        # 메소드 생성
        print("Hi!")

member1 = Member("짱구",5)
# memberInfo = {
#     "name" : "짱구", # 프로퍼티(property) - 객체 안에있는 일반 값을 프로퍼티라고 함.
#     "age" : 5,
#     "sayHi" : def () { # 메소드(method) - 객체안에있는 함수를 메소드라고 함.
#         print("Hi")
#     }
# }
# 객체에 접근하고 싶다면 변수명.키값 - 클래스가 생성
print(member1.name)
member1.sayHi();
member2 = Member("짱아",3)