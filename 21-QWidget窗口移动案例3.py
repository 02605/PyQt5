from PyQt5.Qt import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.move_flag = 0
        self.setWindowTitle("属性")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        pass

    def mousePressEvent(self, evt):

        # 鼠标左键
        if evt.button() == Qt.MouseButton.LeftButton:
            self.move_flag = 1
            # QMouseEvent
            # 确定鼠标第一次按下的点 ; 确定鼠标当前所在的原始点
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()

            self.origin_x = self.x()
            self.origin_y = self.y()

        # print(self.mouse_x, self.mouse_y)

    def mouseMoveEvent(self, evt):

        if self.move_flag:
            # print(evt.globalX(), evt.globalY())
            # 计算移动向量
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y

            self.move(self.origin_x + move_x, self.origin_y + move_y)


    def mouseReleaseEvent(self, QMouseEvent):

        self.move_flag = 0

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.setMouseTracking(1)
    window.show()
    sys.exit(app.exec_())