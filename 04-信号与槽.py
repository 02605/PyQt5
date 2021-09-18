from PyQt5.Qt import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号与槽")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.test_shuxing()
        self.QObject_xinhao()

    def test_shuxing(self):

        with open("QObject.qss", "r") as f:
            qApp.setStyleSheet(f.read())

        label = QLabel(self)
        label.setText("")

    def QObject_xinhao(self):

        self.obj = QObject()
        # obj.objectNameChanged()
        # def destroy_cao(obj):
        #     print("destoryed", obj)
        # self.obj.destroyed.connect(destroy_cao)
        #
        # del self.obj
        def obj_name_cao(obj_name):
            print("name_changed", obj_name)

        def obj_name_cao2(obj_name):
            print("name_changed", obj_name)

        self.obj.objectNameChanged.connect(obj_name_cao)
        self.obj.objectNameChanged.connect(obj_name_cao2)
        # 槽的数量
        print(self.obj.receivers(self.obj.objectNameChanged))
        self.obj.setObjectName("hello1")
        # print(self.obj.signalsBlocked(), "connect")
        # # self.obj.objectNameChanged.disconnect()
        # self.obj.blockSignals(0)
        # self.obj.setObjectName("hello2")
        # # self.obj.objectNameChanged.connect(obj_name_cao)
        # # 临时阻断
        # self.obj.blockSignals(1)
        # print(self.obj.signalsBlocked(), "disconnect")
        # self.obj.setObjectName("hello3")



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())