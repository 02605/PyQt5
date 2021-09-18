from PyQt5.Qt import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject属性")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.test_shuxing()

    def test_shuxing(self):

        with open("QObject.qss", "r") as f:
            qApp.setStyleSheet(f.read())

        label = QLabel(self)
        label.setObjectName('notice')
        label.setProperty("notice_level", "warning")
        label.setText("我是谁")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())