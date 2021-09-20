# 0导包
from PyQt5.Qt import *
import sys

class Window(QWidget):

    def mousePressEvent(self, evt):

        # print(self.focusWidget())
        # 聚焦到下一个子控件
        # self.focusNextChild()
        # 上一个
        # self.focusPreviousChild()
        # 是否是下一个
        self.focusNextPrevChild(1)




# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = Window()
# 2.2设置控件
window.setWindowTitle("焦点控制")
window.resize(500, 500)

le1 = QLineEdit(window)
le1.move(50, 50)

le2 = QLineEdit(window)
le2.move(150, 150)

le3 = QLineEdit(window)
le3.move(250, 250)

# 聚焦顺序 le1-le3
QWidget.setTabOrder(le1, le3)
QWidget.setTabOrder(le3, le2)

# 设置焦点
# le2.setFocus()
# 设置焦点策略 TAB键
# le3.setFocusPolicy(Qt.TabFocus)

# le3.setFocusPolicy(Qt.ClickFocus)

# tab和单击
# le3.setFocusPolicy(Qt.StrongFocus)

# 只能通过程序setFocus获取焦点
# le3.setFocusPolicy(Qt.NoFocus)

# 清空焦点
# le2.clearFocus()

# 2.3展示控件
window.show()

# print(le1)
# print(le2)
# print(le3)
#
# le1.setFocus()

# 获取当前窗口内部，所有子控件中获取焦点的那个
# print(window.focusWidget())

# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())