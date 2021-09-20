# 0导包
from PyQt5.Qt import *
import sys
# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
# window = QWidget()
window = QMainWindow()
# QMainWindow部分功能控件是懒加载
window.statusBar()
# 2.2设置控件
window.setWindowTitle("信息提示案例")
window.resize(500, 500)
window.setWindowFlags((Qt.WindowContextHelpButtonHint))


#当鼠标停留在窗口控件身上，在状态栏上提示
window.setStatusTip("这是窗口")
print(window.statusTip())

label = QLabel(window)
label.setText("这是一个文本")
label.setStatusTip("我是标签")
label.setToolTip("这是一个提示标签")
print(label.toolTip())

label.setToolTipDuration(2000)
print(label.toolTipDuration())


label.setWhatsThis("我是谁?")


# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())