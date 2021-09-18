from PyQt5.Qt import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("类型判定")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.test_类型案例()

    def test_类型判定(self):

        obj = QObject()
        wei = QWidget()
        btn = QPushButton()
        label = QLabel()

        objs = [obj, wei, btn, label]
        for o in objs:
            # print(o.isWidgetType()) # 判断类型
            print(o.inherits("QLabel")) # 判断继承

    def test_类型案例(self):

        label1 = QLabel(self)
        label1.setText("label1")
        label2 = QLabel(self)
        label2.setText("label2")
        label2.move(100, 100)
        btn = QPushButton(self)
        btn.setText("点我")
        btn.move(200, 200)

        # for widget in self.findChildren(QLabel):
        #     print(widget)

        for widget in self.children():
            if widget.inherits("QLabel"):
                widget.setStyleSheet("background-color: cyan")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())