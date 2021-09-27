# 0导包
from PyQt5.Qt import *
import sys
# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("排他性")
window.resize(500, 500)

for i in range(0, 3):

    btn = QPushButton(window)
    btn.setText("btn" + str(i+1) )
    btn.move(50*i, 50*i)

    # print(btn.autoExclusive())
    # print(btn.isCheckable())
    # 设置能够选中
    btn.setCheckable(1)
    # 设置排他性
    btn.setAutoExclusive(1)

btn = QPushButton(window)
btn.setText("btn4")
btn.move(150, 150)
btn.setCheckable(1)


# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())