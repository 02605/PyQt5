from PyQt5.Qt import *

class Window(QWidget):

    def __init__(self, num_, h_):
        super().__init__()
        self.setWindowTitle("九宫格")
        self.resize(500, 500)
        self.setup_ui(num_, h_)

    def setup_ui(self, num_, h_):

        # 控件的宽度
        w_width = self.width() / h_
        # 总共多少行
        row_count = (num_ - 1) // h_ + 1
        # 控件的高度
        w_height = self.height() / row_count

        for i in range(0, num_):
            w = QWidget(self)
            w.resize(w_width, w_height)
            w.move(i % h_ * w_width, i // h_ * w_height)
            w.setStyleSheet("background-color: green; border: 1px solid yellow;")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window(20, 3)
    window.show()
    sys.exit(app.exec_())