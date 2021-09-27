# 0导包
from PyQt5.Qt import *
import sys
# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("按钮可用信号")
window.resize(500, 500)

btn = QPushButton(window)
btn.setText("可用信号")
btn.move(200, 200)
btn.setCheckable(1)
btn.pressed.connect(lambda : print("按钮被按下"))

btn.released.connect(lambda : print("按钮松开或移出按钮内部"))

# 必须按下并在内部松开 value按钮的选中状态
btn.clicked.connect(lambda value: print("按钮被点击", value))

btn.toggled.connect(lambda value: print("按钮选中状态发生改变", value))


# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())