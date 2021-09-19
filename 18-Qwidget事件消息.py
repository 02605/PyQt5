from PyQt5.Qt import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("事件消息学习")
        self.resize(500, 500)
        self.setup_ui()
        # 设置鼠标跟踪 mouseMoveEvent
        # self.setMouseTracking(0)

    def setup_ui(self):
        pass

    # 窗口关闭事件
    def closeEvent(self, ev):

        print("窗口关闭了")

    def showEvent(self, ev):

        print("窗口打开了")

    def moveEvent(self, QMoveEvent):

        print("窗口移动了")

    def resizeEvent(self, QResizeEvent):

        print("窗口改变了尺寸大小")

    def enterEvent(self, QEvent):

        self.setStyleSheet("background-color: blue;")
        print("鼠标进来了")

    def leaveEvent(self, QEvent):

        self.setStyleSheet("background-color: green;")
        print("鼠标离开了")

    def mousePressEvent(self, QMouseEvent):

        print("鼠标按下了")

    def mouseReleaseEvent(self, QMouseEvent):

        print("鼠标抬起了")

    def mouseDoubleClickEvent(self, QMouseEvent):

        print("双击")

    def mouseMoveEvent(self, QMouseEvent):

        print("鼠标移动")

    def keyPressEvent(self, QKeyEvent):

        print("键盘按下")

    def keyReleaseEvent(self, QKeyEvent):

        print("键盘释放")

    def focusInEvent(self, QFocusEvent):

        print("获取了焦点")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())