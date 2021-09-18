# 0导包
from PyQt5.Qt import *
import sys


class MyLabel(QLabel):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.setText("10")
        self.move(100, 100)
        self.setStyleSheet("font-size: 23px;")


    def setSec(self, sec):

        self.setText(sec)

    def MyStartTimer(self, ms):

        self.timer_id = self.startTimer(ms)

    def timerEvent(self, *args, **kwargs):

        current_sec = int(self.text())
        current_sec -= 1

        self.setText(str(current_sec))
        if current_sec == 0:
            print("stop")
            self.killTimer(self.timer_id)

# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("定时器案例")
window.resize(500, 500)

label = MyLabel(window)
label.setSec("6")
label.MyStartTimer(600)

# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())