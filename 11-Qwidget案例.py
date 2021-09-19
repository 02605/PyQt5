import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)
# 包括外层边框
window.move(300, 300)


window.show()


sys.exit(app.exec_())