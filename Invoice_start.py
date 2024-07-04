from PyQt5 import QtCore, QtWidgets
from main import window_controller


if __name__ == '__main__':
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    
    window = window_controller()
    window.show()
    
    sys.exit(app.exec_())