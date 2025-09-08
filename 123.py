import tkinter as tk

class RectangleDrawer:
    def __init__(self, master):
        self.master = master
        self.master.title("그림판 스타일 직사각형 그리기")

        self.canvas = tk.Canvas(master, bg="white", width=600, height=400)
        self.canvas.pack()

        self.start_x = None
        self.start_y = None
        self.rect = None

        # 마우스 이벤트 바인딩
        self.canvas.bind("<Button-1>", self.on_button_press)      # 마우스 눌렀을 때
        self.canvas.bind("<B1-Motion>", self.on_move_press)       # 드래그 중일 때
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)  # 버튼에서 손 뗐을 때

    def on_button_press(self, event):
        # 시작 좌표 기록
        self.start_x = event.x
        self.start_y = event.y

        # 직사각형 하나 만들고 나중에 업데이트
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='black')

    def on_move_press(self, event):
        # 마우스 드래그 중: 직사각형 크기 갱신
        cur_x, cur_y = event.x, event.y
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        # 드래그 종료 시: 좌표 확정
        pass  # 필요시 로그를 남기거나 다른 작업 추가 가능

# 실행
root = tk.Tk()
app = RectangleDrawer(root)
root.mainloop()
