from PyQt5.Qt import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("控件交互案例")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        # 三个子控件
        qLineEdit = QLineEdit(self)
        # qLineEdit.setText("")
        qLineEdit.move(100, 100)

        label = QLabel(self)
        label.setText("标签")
        label.move(100, 50)
        label.hide()

        btn = QPushButton(self)
        btn.setText("登录")
        btn.move(100, 150)
        btn.setEnabled(0)

        def text_cao(text):

            # if len(text) > 0:
            #     btn.setEnabled(1)
            # else:
            #     btn.setEnabled(0)
            btn.setEnabled(len(text))
            print("文本内容改变", text)

        qLineEdit.textChanged.connect(text_cao)


        def btn_check():

            # if qLineEdit.text() == "rx":
            #     label.setText("登录成功")
            # else:
            #     label.setText("登录失败")
            label.setText("登录成功") if qLineEdit.text() == "rx" else label.setText("登录失败")
            label.adjustSize() # 初始化已经设置了大小，这一步让控件再次改变大小
            label.show()
            # print("按钮点击了")

        btn.pressed.connect(btn_check)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())