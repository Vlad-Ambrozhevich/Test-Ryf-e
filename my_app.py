from instr import *
from second_win import *
class MainWin(QWidget):
app = QApplication([])
mw = MainWin()
app.exec_()
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self. hello_text = QLabel(txt_hello)
        self. txt_instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)
    def connects(self):
        self.bnt_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
