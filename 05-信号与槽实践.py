from PyQt5.Qt import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号与槽实践")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.test_xinhao()
        self.test_xinhao2()

    def test_xinhao(self):
        # 按钮点击槽
        btn = QPushButton(self)
        btn.setText("我是按钮")
        btn.move(200,200)
        def cao_():
            print("点我了")
        btn.clicked.connect(cao_)

    def test_xinhao2(self):
        # 连接窗口标题变化的信号与槽
        def cao_(title_name):
            print(title_name)
            self.blockSignals(1) # 临时中止
            # self.windowTitleChanged.disconnect() 取消连接
            self.setWindowTitle("RosebudX-"+title_name)
            # self.windowTitleChanged.connect(cao_)
            self.blockSignals(0)


        self.windowTitleChanged.connect(cao_)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.setWindowTitle("hello1")
    window.setWindowTitle("hello2")
    sys.exit(app.exec_())