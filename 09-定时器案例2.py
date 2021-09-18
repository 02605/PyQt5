# 0导包
from PyQt5.Qt import *
import sys

class MyQWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("定时器案例2")
        self.resize(500, 500)
        self.startTimer(100)

    def timerEvent(self, a0: 'QTimerEvent'):
        current_w = self.width()
        current_h = self.height()
        self.resize(current_w + 10, current_h + 10)

# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = MyQWidget()

# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())