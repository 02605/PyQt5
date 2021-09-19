# 0导包
from PyQt5.Qt import *
import sys


class Label(QLabel):

    def enterEvent(self, QEvent):

        self.setText("欢迎光临")
        print("鼠标进入")

    def leaveEvent(self, QEvent):

        self.setText("谢谢惠顾")
        print("鼠标离开")

# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("鼠标操作案例1")
window.resize(500, 500)

label = Label(window)
label.setText("")
label.move(200, 200)
label.resize(200, 200)
label.setStyleSheet("background-color: cyan;")

# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())