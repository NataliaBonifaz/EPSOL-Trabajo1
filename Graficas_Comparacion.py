# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graficas_comparación.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_comparation_options(object):
    def setupUi(self, comparation_options):
        comparation_options.setObjectName("comparation_options")
        comparation_options.resize(401, 454)
        self.list_1 = QtWidgets.QComboBox(comparation_options)
        self.list_1.setGeometry(QtCore.QRect(170, 120, 181, 31))
        self.list_1.setObjectName("list_1")
        self.list_2 = QtWidgets.QComboBox(comparation_options)
        self.list_2.setGeometry(QtCore.QRect(170, 180, 181, 31))
        self.list_2.setObjectName("list_2")
        self.titte_label = QtWidgets.QLabel(comparation_options)
        self.titte_label.setGeometry(QtCore.QRect(30, 30, 340, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.titte_label.setFont(font)
        self.titte_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.titte_label.setAlignment(QtCore.Qt.AlignCenter)
        self.titte_label.setObjectName("titte_label")
        self.variable_1_label = QtWidgets.QLabel(comparation_options)
        self.variable_1_label.setGeometry(QtCore.QRect(20, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.variable_1_label.setFont(font)
        self.variable_1_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.variable_1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.variable_1_label.setObjectName("variable_1_label")
        self.variable_2_label = QtWidgets.QLabel(comparation_options)
        self.variable_2_label.setGeometry(QtCore.QRect(20, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.variable_2_label.setFont(font)
        self.variable_2_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.variable_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.variable_2_label.setObjectName("variable_2_label")
        self.ok_button = QtWidgets.QPushButton(comparation_options)
        self.ok_button.setGeometry(QtCore.QRect(150, 290, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ok_button.setFont(font)
        self.ok_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_button.setObjectName("ok_button")
        self.cancel_button = QtWidgets.QPushButton(comparation_options)
        self.cancel_button.setGeometry(QtCore.QRect(260, 290, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.cancel_button.setFont(font)
        self.cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_button.setObjectName("cancel_button")
        self.logo_label = QtWidgets.QLabel(comparation_options)
        self.logo_label.setGeometry(QtCore.QRect(20, 360, 131, 71))
        self.logo_label.setStyleSheet("border-image: url(:/EPSOL/LogoEpsolCMYK.png);")
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")

        self.retranslateUi(comparation_options)
        QtCore.QMetaObject.connectSlotsByName(comparation_options)

    def retranslateUi(self, comparation_options):
        _translate = QtCore.QCoreApplication.translate
        comparation_options.setWindowTitle(_translate("comparation_options", "Dialog"))
        self.titte_label.setText(_translate("comparation_options", "Comparación de Variables"))
        self.variable_1_label.setText(_translate("comparation_options", "Variable 1"))
        self.variable_2_label.setText(_translate("comparation_options", "Variable 2"))
        self.ok_button.setToolTip(_translate("comparation_options", "Genera reporte en word"))
        self.ok_button.setText(_translate("comparation_options", "Graficar"))
        self.cancel_button.setToolTip(_translate("comparation_options", "Genera reporte en word"))
        self.cancel_button.setText(_translate("comparation_options", "Cancelar"))
import Epsol_Logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    comparation_options = QtWidgets.QDialog()
    ui = Ui_comparation_options()
    ui.setupUi(comparation_options)
    comparation_options.show()
    sys.exit(app.exec_())