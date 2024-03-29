# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.MainGroupBox.setGeometry(QtCore.QRect(40, 40, 731, 481))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.MainGroupBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("UnPilgia")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.MainGroupBox.setFont(font)
        self.MainGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.MainGroupBox.setObjectName("MainGroupBox")
        self.LessonsGroupBox = QtWidgets.QGroupBox(self.MainGroupBox)
        self.LessonsGroupBox.setGeometry(QtCore.QRect(340, 130, 331, 271))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.LessonsGroupBox.setFont(font)
        self.LessonsGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.LessonsGroupBox.setObjectName("LessonsGroupBox")
        self.LessonsListView = QtWidgets.QListView(self.LessonsGroupBox)
        self.LessonsListView.setGeometry(QtCore.QRect(40, 70, 256, 192))
        font = QtGui.QFont()
        font.setFamily("UnShinmun")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.LessonsListView.setFont(font)
        self.LessonsListView.setObjectName("LessonsListView")
        self.AddLessonButton = QtWidgets.QPushButton(self.MainGroupBox)
        self.AddLessonButton.setGeometry(QtCore.QRect(70, 190, 131, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.AddLessonButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("UnShinmun")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.AddLessonButton.setFont(font)
        self.AddLessonButton.setObjectName("AddLessonButton")
        self.DeleteLessonButton = QtWidgets.QPushButton(self.MainGroupBox)
        self.DeleteLessonButton.setGeometry(QtCore.QRect(70, 270, 131, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.DeleteLessonButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("UnShinmun")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.DeleteLessonButton.setFont(font)
        self.DeleteLessonButton.setObjectName("DeleteLessonButton")
        self.EnterLessonButton = QtWidgets.QPushButton(self.MainGroupBox)
        self.EnterLessonButton.setGeometry(QtCore.QRect(70, 350, 131, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.EnterLessonButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("UnShinmun")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.EnterLessonButton.setFont(font)
        self.EnterLessonButton.setObjectName("EnterLessonButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StudyDex"))
        self.MainGroupBox.setTitle(_translate("MainWindow", "StudyDex"))
        self.LessonsGroupBox.setTitle(_translate("MainWindow", "Yours lessons"))
        self.AddLessonButton.setText(_translate("MainWindow", "Add lesson"))
        self.DeleteLessonButton.setText(_translate("MainWindow", "Delete lesson"))
        self.EnterLessonButton.setText(_translate("MainWindow", "Enter lesson"))
