# 0导包
from PyQt5.Qt import *
import sys
# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("按钮模拟点击")
window.resize(500, 500)

btn = QPushButton(window)
btn.setText("我是按钮")
btn.move(200, 200)
btn.pressed.connect(lambda : print("pressed"))

# 触发点击
# btn.click()
# 带动画的点击
# btn.animateClick(2000)

btn2 = QPushButton(window)
btn2.setText("按钮2")

btn2.pressed.connect(lambda : btn.animateClick(1000))



# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())