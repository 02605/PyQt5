import sys
from PyQt5.Qt import *

class MyQWidget(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("鼠标操作案例")
        self.resize(500, 500)
        self.move(1200, 600)
        # 设置鼠标跟踪
        self.setMouseTracking(1)
        # 初始化其他界面
        self.initGui(r"D:\Desktop\233.jpg")



    def initGui(self, icnoPath):

        qp = QPixmap(icnoPath).scaled(50, 50)
        cursor = QCursor(qp)
        self.setCursor(cursor)

        self.label = QLabel(self)
        self.label.setText("LABEL")
        self.label.move(100, 100)
        self.label.setStyleSheet("background-color: cyan;")


    # 重写鼠标移动事件
    def mouseMoveEvent(self, mv):

        print("鼠标移动", mv.localPos())
        # QPointF
        # label = self.findChild(QLabel)
        self.label.move(mv.localPos().x(), mv.localPos().y())


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MyQWidget()

    window.show()

    sys.exit(app.exec_())