class Calculator:
    def __init__(self):
        self.count = 1

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

while True:
    s = input()
    if s == "q":
        break
    try:
        a, c, b = s.split()
        a = int(a)
        b = int(b)
        if c == "+":
            print(f"count: {cll.count} / {cll.add(a, b)}")
        elif c == "-":
            print(f"count: {cll.count} / {cll.sub(a, b)}")
        elif c == "*":
            print(f"count: {cll.count} / {cll.mul(a, b)}")
        elif c == "/":
            print(f"count: {cll.count} / {cll.div(a, b)}")
        else:
            print("invalid")
    except Exception as e:
        print("error", e)