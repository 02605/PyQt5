from PyQt5.Qt import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("对象删除")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.test_del()

    def test_del(self):
        btn = QPushButton(self)
        btn.setText("hello")
        # btn.deleteLater()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())