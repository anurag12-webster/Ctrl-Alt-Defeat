# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\uis\question (1).ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 810)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.questionPanel = QtWidgets.QTextEdit(self.centralwidget)
        self.questionPanel.setGeometry(QtCore.QRect(10, 110, 441, 71))
        self.questionPanel.setObjectName("questionPanel")
        self.option1 = QtWidgets.QRadioButton(self.centralwidget)
        self.option1.setGeometry(QtCore.QRect(30, 270, 82, 17))
        self.option1.setObjectName("option1")
        self.option3 = QtWidgets.QRadioButton(self.centralwidget)
        self.option3.setGeometry(QtCore.QRect(30, 300, 82, 17))
        self.option3.setObjectName("option3")
        self.option3_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.option3_2.setGeometry(QtCore.QRect(30, 330, 82, 17))
        self.option3_2.setObjectName("option3_2")
        self.option4 = QtWidgets.QRadioButton(self.centralwidget)
        self.option4.setGeometry(QtCore.QRect(30, 360, 82, 17))
        self.option4.setObjectName("option4")
        self.examdetails = QtWidgets.QTextEdit(self.centralwidget)
        self.examdetails.setGeometry(QtCore.QRect(0, 0, 971, 101))
        self.examdetails.setObjectName("examdetails")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 60, 251, 41))
        self.textEdit_3.setStyleSheet("\n"
"background-color: rgb(255, 0, 0);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(250, 60, 251, 41))
        self.textEdit_4.setStyleSheet("background-color: rgb(180, 255, 247);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(500, 60, 251, 41))
        self.textEdit_5.setStyleSheet("background-color: rgb(204, 0, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.panel = QtWidgets.QTextEdit(self.centralwidget)
        self.panel.setGeometry(QtCore.QRect(730, 100, 241, 481))
        self.panel.setObjectName("panel")
        self.Question1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question1.setGeometry(QtCore.QRect(760, 170, 41, 20))
        self.Question1.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"background-color: rgb(47, 255, 44);")
        self.Question1.setObjectName("Question1")
        self.panelattemptedquestions = QtWidgets.QTextEdit(self.centralwidget)
        self.panelattemptedquestions.setGeometry(QtCore.QRect(770, 140, 111, 21))
        self.panelattemptedquestions.setObjectName("panelattemptedquestions")
        self.Question2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question2.setGeometry(QtCore.QRect(810, 170, 41, 20))
        self.Question2.setObjectName("Question2")
        self.Question3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question3.setGeometry(QtCore.QRect(860, 170, 41, 20))
        self.Question3.setObjectName("Question3")
        self.Question4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question4.setGeometry(QtCore.QRect(910, 170, 41, 20))
        self.Question4.setObjectName("Question4")
        self.Question5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question5.setGeometry(QtCore.QRect(760, 210, 41, 20))
        self.Question5.setObjectName("Question5")
        self.Question6 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question6.setGeometry(QtCore.QRect(810, 210, 41, 20))
        self.Question6.setObjectName("Question6")
        self.Question7 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question7.setGeometry(QtCore.QRect(860, 210, 41, 20))
        self.Question7.setObjectName("Question7")
        self.Question8 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question8.setGeometry(QtCore.QRect(910, 210, 41, 20))
        self.Question8.setObjectName("Question8")
        self.Question9 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question9.setGeometry(QtCore.QRect(760, 260, 41, 20))
        self.Question9.setObjectName("Question9")
        self.Question10 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question10.setGeometry(QtCore.QRect(810, 260, 41, 21))
        self.Question10.setObjectName("Question10")
        self.Question11 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question11.setGeometry(QtCore.QRect(860, 260, 41, 20))
        self.Question11.setObjectName("Question11")
        self.Question12 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Question12.setGeometry(QtCore.QRect(910, 260, 41, 20))
        self.Question12.setObjectName("Question12")
        self.bottompanelbox = QtWidgets.QTextEdit(self.centralwidget)
        self.bottompanelbox.setGeometry(QtCore.QRect(10, 650, 991, 81))
        self.bottompanelbox.setObjectName("bottompanelbox")
        self.previous = QtWidgets.QPushButton(self.centralwidget)
        self.previous.setGeometry(QtCore.QRect(20, 660, 75, 23))
        self.previous.setObjectName("previous")
        self.savenextbutton = QtWidgets.QPushButton(self.centralwidget)
        self.savenextbutton.setGeometry(QtCore.QRect(300, 660, 75, 23))
        self.savenextbutton.setObjectName("savenextbutton")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(104, 660, 91, 23))
        self.next.setObjectName("next")
        self.mark = QtWidgets.QPushButton(self.centralwidget)
        self.mark.setGeometry(QtCore.QRect(200, 660, 91, 23))
        self.mark.setObjectName("mark")
        self.submitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.submitbutton.setGeometry(QtCore.QRect(820, 500, 75, 23))
        self.submitbutton.setObjectName("submitbutton")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(870, 700, 111, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.diagrmbox = QtWidgets.QTextEdit(self.centralwidget)
        self.diagrmbox.setGeometry(QtCore.QRect(30, 190, 104, 71))
        self.diagrmbox.setObjectName("diagrmbox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(880, 0, 81, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(".\\uis\\../../Users/Lenovo/Downloads/WhatsApp Image 2023-09-10 at 12.35.47 PM (1).jpg"))
        self.label_3.setObjectName("label_3")
        self.plainTextEdit_13 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_13.setGeometry(QtCore.QRect(780, 340, 41, 20))
        self.plainTextEdit_13.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"background-color: rgb(47, 255, 44);")
        self.plainTextEdit_13.setObjectName("plainTextEdit_13")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(830, 340, 104, 20))
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit_16 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_16.setGeometry(QtCore.QRect(780, 370, 41, 20))
        self.plainTextEdit_16.setAutoFillBackground(False)
        self.plainTextEdit_16.setStyleSheet("background-color: rgb(50rgb(253, 0, 0), 85, 0);\n"
"background-color: rgb(255, 6, 39);")
        self.plainTextEdit_16.setObjectName("plainTextEdit_16")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(830, 370, 104, 20))
        self.textEdit_2.setObjectName("textEdit_2")
        self.plainTextEdit_17 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_17.setGeometry(QtCore.QRect(780, 400, 41, 20))
        self.plainTextEdit_17.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.plainTextEdit_17.setObjectName("plainTextEdit_17")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(830, 400, 104, 20))
        self.textEdit_6.setObjectName("textEdit_6")
        self.plainTextEdit_18 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_18.setGeometry(QtCore.QRect(780, 430, 41, 20))
        self.plainTextEdit_18.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"background-color:rgb(170, 255, 255);")
        self.plainTextEdit_18.setObjectName("plainTextEdit_18")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(830, 430, 104, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(760, 110, 171, 20))
        self.label_4.setObjectName("label_4")
        self.Userprofile = QtWidgets.QTextEdit(self.centralwidget)
        self.Userprofile.setGeometry(QtCore.QRect(830, 10, 104, 71))
        self.Userprofile.setObjectName("Userprofile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.questionPanel.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Question 1 </p></body></html>"))
        self.option1.setText(_translate("MainWindow", "option 1"))
        self.option3.setText(_translate("MainWindow", "option2 "))
        self.option3_2.setText(_translate("MainWindow", "option3 "))
        self.option4.setText(_translate("MainWindow", "option 4"))
        self.examdetails.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Aptitude test </span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#090909;\">Quantitative aptitude</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">verbal ability</p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">verbal reasoning</p></body></html>"))
        self.Question1.setPlainText(_translate("MainWindow", "Q1"))
        self.panelattemptedquestions.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Questions </p></body></html>"))
        self.Question2.setPlainText(_translate("MainWindow", "Q2"))
        self.Question3.setPlainText(_translate("MainWindow", "Q3"))
        self.Question4.setPlainText(_translate("MainWindow", "Q4\n"
""))
        self.Question5.setPlainText(_translate("MainWindow", "Q5"))
        self.Question6.setPlainText(_translate("MainWindow", "Q6"))
        self.Question7.setPlainText(_translate("MainWindow", "Q7"))
        self.Question8.setPlainText(_translate("MainWindow", "Q8\n"
""))
        self.Question9.setPlainText(_translate("MainWindow", "Q9"))
        self.Question10.setPlainText(_translate("MainWindow", "Q10"))
        self.Question11.setPlainText(_translate("MainWindow", "Q11"))
        self.Question12.setPlainText(_translate("MainWindow", "Q12"))
        self.previous.setText(_translate("MainWindow", "Previous"))
        self.savenextbutton.setText(_translate("MainWindow", "save& next"))
        self.next.setText(_translate("MainWindow", "Mark as Review"))
        self.mark.setText(_translate("MainWindow", "Clear Response"))
        self.submitbutton.setText(_translate("MainWindow", "submit"))
        self.pushButton_6.setText(_translate("MainWindow", "Read instruction"))
        self.diagrmbox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">diagram</p></body></html>"))
        self.plainTextEdit_13.setPlainText(_translate("MainWindow", "1"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Answered</span></p></body></html>"))
        self.plainTextEdit_16.setPlainText(_translate("MainWindow", "0"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Not Answered</span></p></body></html>"))
        self.plainTextEdit_17.setPlainText(_translate("MainWindow", "0"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Not Visited</span></p></body></html>"))
        self.plainTextEdit_18.setPlainText(_translate("MainWindow", "0"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Mark For Review</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Time left for entire exam-00:00:00"))
        self.Userprofile.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">User profile</p></body></html>"))
