# 0导包
from PyQt5.Qt import *
import sys


class Label(QLabel):

    # QKeyEvent
    def keyReleaseEvent(self, evt):

        # print("键盘释放")
        pass

    def keyPressEvent(self, evt):

        # print("键盘按下")
        if evt.key() == Qt.Key.Key_Tab:
            print("用户按下了TAB")

        # ctrl+s
        if evt.modifiers() == Qt.ControlModifier and \
                evt.key() == Qt.Key.Key_S:
            print("ctrl+s")

        # ctrl+shift+s
        if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and \
                evt.key() == Qt.Key.Key_S:
            print("ctrl+shift+s")

# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("键盘操作案例1")
window.resize(500, 500)

label = Label(window)
label.move(100, 100)
label.resize(200, 200)
label.setStyleSheet("background-color: cyan;")
label.grabKeyboard() # 捕获键盘


# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())