# 0导包
from PyQt5.Qt import *
import sys
# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("自动重复")
window.resize(500, 500)

btn = QPushButton(window)
btn.setText("1")

btn.setShortcut("Alt+s")

btn.setAutoRepeat(1)
# 自动重复检测间隔 毫秒（5s执行一次）
btn.setAutoRepeatInterval(5000)
# 首次延迟
btn.setAutoRepeatDelay(2000)
btn.clicked.connect(lambda : btn.setText(str(eval(btn.text()) + 1)))
# btn.pressed.connect(lambda : btn.setText(str(eval(btn.text()) + 1)))


print(btn.autoRepeat())
print(btn.autoRepeatDelay())
print(btn.autoRepeatInterval())


# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())