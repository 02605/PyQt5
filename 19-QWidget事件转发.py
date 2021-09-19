# 0导包
from PyQt5.Qt import *
import sys

class Window(QWidget):

    def mousePressEvent(self, QMouseEvent):

        print("顶层窗口鼠标按下")

class MidWindow(QWidget):

    def mousePressEvent(self, QMouseEvent):

        print("中间控件被按下")

class Label(QLabel):

    def mousePressEvent(self, evt):

        print("标签控件鼠标按下")
        # print(evt.isAccepted())
        # 标识事件已经处理
        # evt.accept()
        # 标识事件没处理（往父对象传递）
        evt.ignore()

# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = Window()
# 2.2设置控件
window.setWindowTitle("事件转发")
window.resize(500, 500)

mid_window = MidWindow(window)
mid_window.resize(300, 300)
# 继承后qss失效了，需要手动开启
mid_window.setAttribute(Qt.WA_StyledBackground, 1)
mid_window.setStyleSheet("background-color: yellow;")

label = Label(mid_window)
# label = QLabel(mid_window)
label.setText("我是标签")
label.setStyleSheet("background-color: red;")
label.move(100, 100)

btn = QPushButton(mid_window)
btn.setText("按钮")
btn.move(50, 50)

# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())