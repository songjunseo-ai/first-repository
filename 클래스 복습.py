class Shape:
    def __init__(self, name = "Unknown"): # 생성자
        self.name = name

    def SetName(self, name): # 이름 변경
        self.name = name

    def Print(self): # 정보 출력
        print(f"이름 : {self.name}")

class Circle(Shape):
    def __init__(self, x, y, radius, name = "Unknown"): # 생성자
        super().__init__(name) # Shape.__init__(self, name)
        self.x = x
        self.y = y
        self.radius = radius

    def GetArea(self): # 면적 계산
        return 3.14 * self.radius ** 2

    def Print(self): # 정보 출력
        super().Print() # 부모 클래스의 메소드 호출 = Shape.Print(self)
        print(f"면적 : {self.GetArea()}")

class Rect(Shape):
    def __init__(self, x1, y1, x2, y2, name = "rect1"):
        super().__init__(name)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def get_area(self):
        return (self.x2-self.x1)*(self.y2-self.y1)
    def __str__(self):
        return f"(면적 : {self.get_area()})"
    def Print(self):
        super().Print()
        print(f"면적 : {self.get_area()}")


Rect1 = Rect(1,1,2,2)
Rect1.SetName("김치")
Rect1.Print()