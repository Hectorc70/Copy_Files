# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_copy.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 383)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.text_origen = QtWidgets.QLabel(self.centralwidget)
        self.text_origen.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.text_origen.setObjectName("text_origen")
        self.copiar_subdirectorios = QtWidgets.QRadioButton(self.centralwidget)
        self.copiar_subdirectorios.setGeometry(QtCore.QRect(20, 170, 131, 17))
        self.copiar_subdirectorios.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.copiar_subdirectorios.setChecked(False)
        self.copiar_subdirectorios.setObjectName("copiar_subdirectorios")
        self.ruta_origen = QtWidgets.QLineEdit(self.centralwidget)
        self.ruta_origen.setGeometry(QtCore.QRect(100, 20, 421, 20))
        self.ruta_origen.setObjectName("ruta_origen")
        self.text_destino = QtWidgets.QLabel(self.centralwidget)
        self.text_destino.setGeometry(QtCore.QRect(20, 90, 81, 16))
        self.text_destino.setObjectName("text_destino")
        self.ruta_destino = QtWidgets.QLineEdit(self.centralwidget)
        self.ruta_destino.setGeometry(QtCore.QRect(100, 90, 421, 20))
        self.ruta_destino.setObjectName("ruta_destino")
        self.text_hilos_trabajo = QtWidgets.QLabel(self.centralwidget)
        self.text_hilos_trabajo.setGeometry(QtCore.QRect(20, 130, 81, 16))
        self.text_hilos_trabajo.setObjectName("text_hilos_trabajo")
        self.numero_hilos = QtWidgets.QSpinBox(self.centralwidget)
        self.numero_hilos.setGeometry(QtCore.QRect(100, 130, 42, 22))
        self.numero_hilos.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.numero_hilos.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.numero_hilos.setMaximum(5)
        self.numero_hilos.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.numero_hilos.setObjectName("numero_hilos")
        self.boton_start = QtWidgets.QPushButton(self.centralwidget)
        self.boton_start.setGeometry(QtCore.QRect(220, 210, 151, 41))
        self.boton_start.setObjectName("boton_start")
        self.crear_log = QtWidgets.QRadioButton(self.centralwidget)
        self.crear_log.setGeometry(QtCore.QRect(150, 170, 82, 17))
        self.crear_log.setObjectName("crear_log")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CopyFiles"))
        self.text_origen.setText(_translate("MainWindow", "Carpeta Origen"))
        self.copiar_subdirectorios.setText(_translate("MainWindow", "SUBDIRECTORIOS"))
        self.text_destino.setText(_translate("MainWindow", "Carpeta Destino"))
        self.text_hilos_trabajo.setText(_translate("MainWindow", "Numero de hilos"))
        self.boton_start.setText(_translate("MainWindow", "Empezar"))
        self.crear_log.setText(_translate("MainWindow", "RadioButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())