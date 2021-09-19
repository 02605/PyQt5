# 0导包
from PyQt5.Qt import *
import sys


class MyWindow(QWidget):

    # QMouseEvent

    def mouseMoveEvent(self, me):

        # me.localPos()局部位置
        # me.globalPos()全局位置

        print("鼠标移动了", me.localPos())

# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = MyWindow()
# 2.2设置控件
window.setWindowTitle("鼠标跟踪")
window.resize(500, 500)
# 设置鼠标跟踪
window.setMouseTracking(1)
print(window.hasMouseTracking())



# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())