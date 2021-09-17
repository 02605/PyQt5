# 0导包
from PyQt5.Qt import * # 常用类汇总
import sys #

# 命令行启动程序时，可以接收命令行传递的参数
# argvs = sys.argv

# 程序退出方式
# sys.exit()

# 1.创建一个应用程序对象
app = QApplication(sys.argv)
# print(app.arguments()) # 打印app的参数
# 全局的 app对象
# print(qApp.arguments())

# 2.控件的操作
# 创建控件，设置控件属性，事件，信号等
# 2.1创建控件
# 当创建一个控件后，如果这个控件没有父控件，则把他当作顶层控件，系统会自动会给窗口添加一些装饰（标题栏，图标等）
window = QWidget()
# window = QPushButton()
# window = QLabel()
# 2.2设置控件
# window.setText("hello")
window.setWindowTitle("你好qt")
window.resize(400, 400)

# 控件可以作为一个容器（承载其他控件）
label = QLabel(window)
label.setText("我是label")
label.move(100, 100)
# label.setWindowTitle("label")
# label.show()



# 2.3展示控件
# 刚创建的控件，没有父控件，默认情况下是不会被展示的，只能调用show
window.show()



# 3.应用程序的执行，进入到消息循环，程序不会退出（无限循环）
# 检测用户对程序的交互信息 app.exec_()
sys.exit(app.exec_()) # 程序退出返回给主程序