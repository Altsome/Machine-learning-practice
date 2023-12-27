class Calculator:
    def __init__(self):
        self.count = 1

    def calculate(self, x, y, op):
        methods = {
            "+": self.add,
            "-": self.sub,
            "*": self.mul,
            "/": self.div,
        }
        if op not in methods:
            print("invalid")
        return methods[op](x, y)

    def add(self, x, y):
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

cll = Calculator() #instance 생성
def print_result(count, result):
    print(f"count: {count} / {result}")


while True:
    s = input()
    if s == "q":
        break
    try:
        a, c, b = s.split()
        a = int(a)
        b = int(b)
        print_result(cll.count, cll.calculate(a, b, c))
    except Exception as e:
        print("error", e)
