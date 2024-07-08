# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'invoice_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Invoice(object):
    def setupUi(self, Invoice):
        Invoice.setObjectName("Invoice")
        Invoice.resize(418, 488)
        self.gridLayout_2 = QtWidgets.QGridLayout(Invoice)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.container = QtWidgets.QFrame(Invoice)
        self.container.setStyleSheet(".QFrame{\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.gridLayout = QtWidgets.QGridLayout(self.container)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.container)
        self.label_2.setMinimumSize(QtCore.QSize(0, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color: red;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.container)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(50, 35))
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("min-width: 50px;")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.tax_text = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tax_text.sizePolicy().hasHeightForWidth())
        self.tax_text.setSizePolicy(sizePolicy)
        self.tax_text.setMinimumSize(QtCore.QSize(250, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.tax_text.setFont(font)
        self.tax_text.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tax_text.setStyleSheet("")
        self.tax_text.setObjectName("tax_text")
        self.horizontalLayout_3.addWidget(self.tax_text)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.invoice_b_text = QtWidgets.QLabel(self.widget_2)
        self.invoice_b_text.setMinimumSize(QtCore.QSize(50, 35))
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.invoice_b_text.setFont(font)
        self.invoice_b_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.invoice_b_text.setStyleSheet("min-width: 50px;")
        self.invoice_b_text.setObjectName("invoice_b_text")
        self.horizontalLayout_2.addWidget(self.invoice_b_text)
        self.invoice_b_num = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoice_b_num.sizePolicy().hasHeightForWidth())
        self.invoice_b_num.setSizePolicy(sizePolicy)
        self.invoice_b_num.setMinimumSize(QtCore.QSize(256, 32))
        self.invoice_b_num.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.invoice_b_num.setFont(font)
        self.invoice_b_num.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.invoice_b_num.setObjectName("invoice_b_num")
        self.horizontalLayout_2.addWidget(self.invoice_b_num)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.frame)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.invoice_e_text = QtWidgets.QLabel(self.widget_3)
        self.invoice_e_text.setMinimumSize(QtCore.QSize(50, 35))
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(11)
        self.invoice_e_text.setFont(font)
        self.invoice_e_text.setStyleSheet("min-width: 50px;")
        self.invoice_e_text.setObjectName("invoice_e_text")
        self.horizontalLayout.addWidget(self.invoice_e_text)
        self.invoice_e_num = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoice_e_num.sizePolicy().hasHeightForWidth())
        self.invoice_e_num.setSizePolicy(sizePolicy)
        self.invoice_e_num.setMinimumSize(QtCore.QSize(256, 32))
        self.invoice_e_num.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.invoice_e_num.setFont(font)
        self.invoice_e_num.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.invoice_e_num.setObjectName("invoice_e_num")
        self.horizontalLayout.addWidget(self.invoice_e_num)
        self.verticalLayout.addWidget(self.widget_3)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.container)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.frame_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.open = QtWidgets.QPushButton(self.widget_4)
        self.open.setMinimumSize(QtCore.QSize(80, 35))
        self.open.setMaximumSize(QtCore.QSize(80, 35))
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(11)
        self.open.setFont(font)
        self.open.setFocusPolicy(QtCore.Qt.TabFocus)
        self.open.setObjectName("open")
        self.horizontalLayout_4.addWidget(self.open)
        self.open_text = QtWidgets.QTextBrowser(self.widget_4)
        self.open_text.setMinimumSize(QtCore.QSize(256, 40))
        self.open_text.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.open_text.setFont(font)
        self.open_text.setFocusPolicy(QtCore.Qt.NoFocus)
        self.open_text.setStyleSheet("")
        self.open_text.setObjectName("open_text")
        self.horizontalLayout_4.addWidget(self.open_text)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.frame_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.save = QtWidgets.QPushButton(self.widget_5)
        self.save.setMinimumSize(QtCore.QSize(80, 35))
        self.save.setMaximumSize(QtCore.QSize(80, 35))
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(11)
        self.save.setFont(font)
        self.save.setFocusPolicy(QtCore.Qt.TabFocus)
        self.save.setObjectName("save")
        self.horizontalLayout_5.addWidget(self.save)
        self.save_text = QtWidgets.QTextBrowser(self.widget_5)
        self.save_text.setMinimumSize(QtCore.QSize(256, 40))
        self.save_text.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.save_text.setFont(font)
        self.save_text.setFocusPolicy(QtCore.Qt.NoFocus)
        self.save_text.setObjectName("save_text")
        self.horizontalLayout_5.addWidget(self.save_text)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.frame_3)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.start = QtWidgets.QPushButton(self.widget_6)
        self.start.setMinimumSize(QtCore.QSize(80, 40))
        self.start.setMaximumSize(QtCore.QSize(65, 31))
        self.start.setFocusPolicy(QtCore.Qt.TabFocus)
        self.start.setObjectName("start")
        self.horizontalLayout_6.addWidget(self.start)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)
        self.output_text = QtWidgets.QLabel(self.container)
        self.output_text.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.output_text.setFont(font)
        self.output_text.setStyleSheet("QLabel{\n"
"    color: green;\n"
"}")
        self.output_text.setText("")
        self.output_text.setObjectName("output_text")
        self.gridLayout.addWidget(self.output_text, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.container, 0, 0, 1, 1)

        self.retranslateUi(Invoice)
        QtCore.QMetaObject.connectSlotsByName(Invoice)
        Invoice.setTabOrder(self.tax_text, self.invoice_b_num)
        Invoice.setTabOrder(self.invoice_b_num, self.invoice_e_num)
        Invoice.setTabOrder(self.invoice_e_num, self.open)
        Invoice.setTabOrder(self.open, self.save)
        Invoice.setTabOrder(self.save, self.start)

    def retranslateUi(self, Invoice):
        _translate = QtCore.QCoreApplication.translate
        Invoice.setWindowTitle(_translate("Invoice", "未開立電子發票區間整理"))
        self.label_2.setText(_translate("Invoice", "tax_ID.txt存放統一編號選單"))
        self.label.setText(_translate("Invoice", "統一編號："))
        self.invoice_b_text.setText(_translate("Invoice", "發票起號："))
        self.invoice_e_text.setText(_translate("Invoice", "發票訖號："))
        self.open.setText(_translate("Invoice", "開啓檔案"))
        self.save.setText(_translate("Invoice", "存放路徑"))
        self.start.setText(_translate("Invoice", "開始"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Invoice = QtWidgets.QWidget()
    ui = Ui_Invoice()
    ui.setupUi(Invoice)
    Invoice.show()
    sys.exit(app.exec_())
