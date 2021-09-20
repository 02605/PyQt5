# 0导包
from PyQt5.Qt import *
import sys
# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("[*]被编辑状态")
window.resize(500, 500)

window.setWindowModified(1)
# print(window.isWindowModified())

w2 = QWidget()
w2.show()

# 2.3展示控件
window.show()

# w2窗口上升
w2.raise_()

# 是否为活跃窗口
print(window.isActiveWindow())


# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())