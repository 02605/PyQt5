# 0导包
from PyQt5.Qt import *
import sys
# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("父子关系学习")
window.resize(500, 500)

label1 = QLabel(window)
label1.setText("标签1")
label1.move(200, 200)

label2 = QLabel(window)
label2.setText("标签2")
label2.move(50, 50)

label3 = QLabel(window)
label3.setText("标签3")
label3.move(100, 100)

print(window.childAt(50, 50))
print(label2.parentWidget())
# 子控件区域
print(window.childrenRect())

# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())