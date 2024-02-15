class Calculator:
    def __init__(self):     # __init__ : 컨스트럭터, 인스턴스화를 시행하면 무조건 실행됨
        self.count = 1

    def calculate(self, x, y, op):  # 메소드: class안의 함수
        methods = {
            "+": self.add,  # 함수의 이름만 가져온다, ()를 안붙여서 함수를 불러오는 것은 X
            "-": self.sub,
            "*": self.mul,
            "/": self.div,
            "**": self.pow
        }
        if op not in methods:   # if else문은 보통 else를 생략하고 쓴다
            print("invalid")
        return methods[op](x, y)

    def add(self, x, y):    # self를 쓰는 이유: 클래스 내의 인스턴스라고 명시하기 위해서
        self.count += 1
        return x + y

    def sub(self, x, y):
        self.count += 1
        return x - y

    def mul(self, x, y):
        self.count += 1
        return x * y

    def div(self, x, y):
        self.count += 1
        if y == 0:
            return None
        else:
            return x / y

    def pow(self, x, y):
        return x**y


cll = Calculator() # cll instance 생성, 클래스의 모든 것을 불러옴


def print_result(count, result):
    print(f"count: {count} / {result}")     # 문자열 포멧팅


while True:
    s = input()
    if s == "q":
        break
    try:    # try, except 구문: 아래 코드를 돌려보고 에러가 나면 except 아래 코드를 실행
        a, op, b = s.split()
        a = int(a)
        b = int(b)
        print_result(cll.count, cll.calculate(a, b, op))
    except Exception as e:  # error 메시지를 처리
        print("error", e)