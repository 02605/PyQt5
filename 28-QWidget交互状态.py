# 0导包
from PyQt5.Qt import *
import sys

class Window(QWidget):

    def paintEvent(self, evt):

        print("窗口绘制了")

        return super().paintEvent(evt)

class Btn(QPushButton):

    def paintEvent(self, evt):

        print("按钮绘制了")

        return super().paintEvent(evt)


# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = Window()
# 2.2设置控件
window.setWindowTitle("交互状态")
window.resize(500, 500)

btn = Btn(window)
btn.setText("按钮")
# btn.pressed.connect(lambda : print("按钮点击了"))
# btn.pressed.connect(lambda : btn.setVisible(0))


# print(btn.isEnabled())
# btn.setEnabled(0)
# print(btn.isEnabled())

# 2.3展示控件
window.show()
# btn.hide()
print(btn.isHidden())
print(btn.isVisible())


btn.setVisible(0)
# 父控件显示的时候，子控件是否跟着被显示
print(btn.isVisibleTo(window))


# window.setVisible(1)
# window.setHidden(0)
# window.hide()

# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())