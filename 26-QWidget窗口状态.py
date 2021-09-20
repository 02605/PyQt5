# 0导包
from PyQt5.Qt import *
import sys

class Window(QWidget):

    def mousePressEvent(self, evt):

        if self.isMaximized():

            self.showNormal()

        else:

            self.showMaximized()


# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = Window()
# 2.2设置控件
window.setWindowTitle("窗口状态")
window.resize(500, 500)

# print(window.windowState() == Qt.WindowNoState)
# WindowMinimized最小化 WindowMmaximized最大
# window.setWindowState(Qt.WindowMinimized)

# w2 = QWidget()
# w2.setWindowTitle("w2")
# w2.show()

# 2.3展示控件
window.show()

# 最大化
# window.showMaximized()
# window.showFullScreen()
# window.showMinimized()

# w2在前，设置活跃
# w2.setWindowState(Qt.WindowActive)

# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())