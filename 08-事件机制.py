from PyQt5.Qt import *
import sys

class App(QApplication):
    
    # QObject事件的接收者，QEvent事件对象
    def notify(self, QObject_, QEvent_):
        if QObject_.inherits("QPushButton") and QEvent_.type() == QEvent.MouseButtonPress:
            print(QObject_, QEvent_)
        return super().notify(QObject_, QEvent_)

class Btn(QPushButton):

    def event(self, evt):
        if evt.type() == QEvent.MouseButtonPress:
            print(evt)
        return super().event(evt)

    def mousePressEvent(self, e):
        print("an")
        return super().mousePressEvent(e)

app = App(sys.argv)

window = QWidget()

btn = Btn(window)
btn.setText("按钮")
btn.move(100, 100)

def cao():
    print("按钮点击了")
btn.pressed.connect(cao)

window.show()

sys.exit(app.exec_())