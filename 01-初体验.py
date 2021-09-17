from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("第一个窗口")

window.resize(500, 500)

window.move(400, 200)

label = QLabel(window)

label.setText("你好")

label.move(200, 200)

window.show()

sys.exit(app.exec_())

