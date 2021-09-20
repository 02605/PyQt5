# 0导包
from PyQt5.Qt import *
import sys


class Window(QWidget):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.setWindowTitle("窗口标志案例")
        self.resize(500, 500)
        # 无边框，无标题栏
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 窗口半透明
        self.setWindowOpacity(0.9)
        self.initGui()

        # 防止鼠标追踪
        self.move_flag = 0


    def initGui(self):

        # 固定按钮大小
        self.btn_width = 60
        self.btn_height = 40
        self.btn_close_height = 10
        # 添加三子控件
        btn_close = QPushButton(self)
        self.btn_close = btn_close
        btn_close.setText("❎")
        btn_close.resize(self.btn_width, self.btn_height)

        btn_max = QPushButton(self)
        self.btn_max = btn_max
        btn_max.setText("口")
        btn_max.resize(self.btn_width, self.btn_height)

        btn_min = QPushButton(self)
        self.btn_min = btn_min
        btn_min.setText("-")
        btn_min.resize(self.btn_width, self.btn_height)

        def max_normal():

            if self.isMaximized():
                self.showNormal()
                btn_max.setText("口")
            else:
                self.showMaximized()
                btn_max.setText("o")


        btn_close.released.connect(self.close)  # 信号与槽
        btn_max.released.connect(max_normal)
        btn_min.released.connect(self.showMinimized)

    # 窗口变化事件
    def resizeEvent(self, QResizeEvent):

        self.btn_close.move(self.width() - self.btn_close.width(), self.btn_close_height)
        self.btn_max.move(self.btn_close.x() - self.btn_max.width(), self.btn_close_height)
        self.btn_min.move(self.btn_max.x() - self.btn_min.width(), self.btn_close_height)

    def mousePressEvent(self, evt):

        if evt.button() == Qt.MouseButton.LeftButton:
            self.move_flag = 1
            # 窗口原始的全局位置
            self.original_x = self.x()
            self.original_y = self.y()
            # 鼠标按下时的全局位置
            self.press_x = evt.globalX()
            self.press_y = evt.globalY()

    def mouseMoveEvent(self, evt):

        if self.move_flag:
            # 计算移动向量
            move_x = evt.globalX() - self.press_x
            move_y = evt.globalY() - self.press_y
            # 移动
            self.move(self.original_x + move_x, self.original_y + move_y)


    def mouseReleaseEvent(self, QMouseEvent):

        self.move_flag = 0

# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1创建控件
# window = QWidget(flags = Qt.FramelessWindowHint) # 无标题无工具栏
window = Window()

# 2.3展示控件
window.show()
# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
sys.exit(app.exec_())