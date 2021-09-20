# 0导包
from PyQt5.Qt import *
import sys

class Btn(QPushButton):

    def paintEvent(self, evt):

        print("按钮被绘制了")

        return super().paintEvent(evt)



# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("控件释放")
window.resize(500, 500)


btn = Btn(window)
btn.setText("按钮")

btn.destroyed.connect(lambda : print("按钮被销毁了"))

# btn.setVisible(1)
# btn.setHidden(1)
# btn.hide()

# btn.deleteLater()

# 关闭时自动释放开启
btn.setAttribute(Qt.WA_DeleteOnClose, 1)

btn.close()

# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())