# 0导包
from PyQt5.Qt import *
import sys
# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle("自定义鼠标")
window.resize(500, 500)

# 图片对象
qp = QPixmap("D:/Desktop/233.jpg")
# 缩放
new_qp = qp.scaled(50, 50)
# 0, 0鼠标的边界
cursor = QCursor(new_qp, 0, 0)
window.setCursor(cursor)

# 鼠标恢复
# window.unsetCursor()

current_cursor = window.cursor()
# 设置鼠标的位置
current_cursor.setPos(1080, 1024)
print(current_cursor.pos())

# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())