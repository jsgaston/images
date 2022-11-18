# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Button.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

import shutil
from shutil import *
import os
import zipfile

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(519, 344)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 130, 113, 32))
        self.pushButton.setStyleSheet("background-color:red;\n"
                                      "color: white;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:black;\n"
                                      "font:bold 14px;\n"
                                      "padding :6px;\n"
                                      "min-width:10px;\n"
                                      "\n"
                                      "\n"
                                      "")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Browse File"))
        self.pushButton.clicked.connect(self.pushButton_handler)


    def pushButton_handler(self):
        print("Button pressed")
        self.open_dialog_box()
        
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()  #ruta y nombre del archivo con tipo archivo
        print("filename",filename)
        path = filename[0]  #nombre del archivo completo
        print("path",path) #directorio del archivo con archivo y extensión .... bien
        dir=os.getcwd()  #directorio a donde alojar el archivo
        # file name with extension
        file_name = os.path.basename(path)  #nombre archivo con extension
        print("filename",filename)
        print("file_name",file_name)
        # file name without extension
        print(os.path.splitext(file_name)[0])
        el_nombre= os.path.splitext(file_name)[0] #nombre del archivo
        dir=os.getcwd()
        print("el_nombre",el_nombre) #nombre del archivo sin extensión
        print("dir",dir)  #solo el directorio
        
        with zipfile.ZipFile(el_nombre+'.zip', 'w',
                     compression=zipfile.ZIP_DEFLATED,
                     compresslevel=9) as zf:
            zf.write(path, arcname=file_name)
            zf.close()
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())