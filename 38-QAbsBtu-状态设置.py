# 0导包
from PyQt5.Qt import *
import sys
# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("Button")
window.resize(500, 500)

push_btn = QPushButton(window)
push_btn.setText("push_btn")
push_btn.move(50, 50)

radio_btn = QRadioButton(window)
radio_btn.setText("radio_btn")
radio_btn.move(50, 100)

check_box = QCheckBox(window)
check_box.setText("check_box")
check_box.move(50, 150)

# 按下状态
# push_btn.setDown(1)
# radio_btn.setDown(1)
# check_box.setDown(1)

push_btn.setStyleSheet("QPushButton:pressed {background-color: cyan;}")

# 设置可以选中
push_btn.setCheckable(1)
# 设置选中
# radio_btn.setChecked(1)
# radio_btn.pressed.connect(lambda : print(radio_btn.isChecked()))
# print(radio_btn.isChecked())

btn = QPushButton(window)
btn.setText("BTN")

def cao_():

    # 状态取反
    radio_btn.toggle()
    # push_btn.toggle()
    check_box.toggle()

    push_btn.setChecked(not push_btn.isChecked())

btn.pressed.connect(cao_)

# 设置不可用
push_btn.setEnabled(0)

# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())