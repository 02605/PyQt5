# 0导包
from PyQt5.Qt import *
import sys
# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("Qwidget")
# 可变大小
# window.resize(500, 500)
# 固定大小
window.setFixedSize(500, 500)
label = QLabel(window)

label.move(100, 100)
label.setText("label")
label.setStyleSheet("background-color: green;")
btn = QPushButton(window)
btn.move(200, 200)
btn.setText("按钮")


def change_():
    content_ = label.text()+"label"
    label.setText(content_)
    # label.resize(label.width() + 100, label.height())
    label.adjustSize()
btn.clicked.connect(change_)

# 2.3展示控件
window.show()
# 设置用户区域的位置
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())