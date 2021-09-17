from PyQt5.Qt import *
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("继承")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("label")



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())



