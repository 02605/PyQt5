# 0导包
from PyQt5.Qt import *
import sys, math
# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("按钮有效区域")
window.resize(500, 500)

class Btn(QPushButton):

    def hitButton(self, point):

        distance_ = math.sqrt(math.pow(self.width()/2 - point.x(), 2) + math.pow(self.height()/2 - point.y(), 2))
        # print(distance_)

        if distance_ < self.width() / 2:
            return 1

        # 点击右半部分才有效
        # if point.x() > self.width() / 2:
        #     # print(point)
        #     # 返回true才会触发点击事件
        #     return 1
        return 0

    def paintEvent(self, evt):

        super().paintEvent(evt)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(150, 100, 200), 6))

        painter.drawEllipse(self.rect())

btn = Btn(window)
btn.resize(200, 200)
btn.move(150, 150)
btn.setText("点击区域")

btn.pressed.connect(lambda :print("pressed"))
print(window.rect())
print(btn.rect())
# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())