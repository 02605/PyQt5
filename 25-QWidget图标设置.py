# 0导包
from PyQt5.Qt import *
import sys


import ctypes
# 告诉windows此程序是主程序，不然任务栏的图标不生效
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("窗口相关的操作")
window.resize(500, 500)

# 设置图标
icon_ = QIcon(r"D:\Desktop\23.jpg")
window.setWindowIcon(icon_)

# 设置不透明度
window.setWindowOpacity(0.6)


print(window.windowIcon())


# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())