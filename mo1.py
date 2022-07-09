class FourCal21:
    def __init__(self, num1, num2): 
        self.first = num1           
        self.second = num2
    def add(self):
        self.result = self.first + self.second
    def div(self):
        self.result = self.first / self.second

class MoreFourCal11(FourCal21): # FourCal2를 상속 받음
    def mul(self):
        self.result = self.first * self.second
    def sub(self):
        self.result = self.first - self.second
    def div(self): # 상속 받은 메서드를 다시 정의 하는 것 : 오버라이딩
        if self.second == 0:
            self.result = 0
        else:
            self.result = self.first / self.second  

PI = 3.141592

def sum1(num1, num2):
    result = num1 + num2
    return result


dddd = MoreFourCal11(100, 20)