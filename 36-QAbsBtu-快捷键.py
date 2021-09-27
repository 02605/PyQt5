# 0导包
from PyQt5.Qt import *
import sys
# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("快捷键")
window.resize(500, 500)

btn = QPushButton(window)

# &b -- alt+b相当于按下
# btn.setText("a&bc")

# 设置快捷键
btn.setShortcut("Alt+a")
btn.clicked.connect(lambda : print("hello"))


# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())