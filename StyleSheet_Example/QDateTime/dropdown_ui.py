# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dropdown.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(624, 413)
        Dialog.setStyleSheet("QDialog,\n"
"QCalendarWidget,\n"
"QCalendarWidget QWidget,\n"
"QListWidget\n"
" {\n"
"    background-color: #ffffbf;\n"
"}\n"
"\n"
"QPushButton {\n"
"    min-width: 30px;\n"
"}\n"
"\n"
"QDialog {\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QListWidget\n"
" {\n"
"    border: none;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton,\n"
"QListWidget::item {\n"
"    padding: 10px 25px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    margin-bottom: 5px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #b2d5ff;\n"
"    color: #000;\n"
"}\n"
"\n"
"\n"
"QPushButton:checked,\n"
"QListWidget::item:selected {\n"
"    background-color: #0075ff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#clear_btn,\n"
"#now_btn {\n"
"    color: #0078d8;\n"
"    padding: 10px 15px;\n"
"}\n"
"\n"
"/* Style for header area  ####################################################\n"
"\n"
"QCalendarWidget QWidget {\n"
"     alternate-background-color: #fff;\n"
"}\n"
"*/ \n"
"\n"
"/* style for top navigation area ###############################################*/ \n"
"\n"
"#qt_calendar_navigationbar {\n"
"    border-bottom: 0px;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"/* style for month change buttons ############################################ */\n"
"\n"
"#qt_calendar_prevmonth, \n"
"#qt_calendar_nextmonth {\n"
"    /* border delete */\n"
"    border: none;  \n"
"    /* delete default icons */\n"
"    qproperty-icon: none; \n"
"    \n"
"    min-width: 25px;\n"
"    max-width: 25px;\n"
"    min-height: 25px;\n"
"    max-height: 25px;\n"
"\n"
"    border-radius: 5px; \n"
"    /* set background transparent */\n"
"    background-color: transparent; \n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* style for pre month button ############################################ */\n"
"\n"
"#qt_calendar_prevmonth {\n"
"    /* set text for button */\n"
"    /*qproperty-text: \">\";*/\n"
"    margin-left:5px;\n"
"    image: url(:/icons/arrow_up.svg);\n"
"}\n"
"\n"
"/* style for next month button ########################################### */\n"
"#qt_calendar_nextmonth {\n"
"    margin-right:5px;\n"
"    image: url(:/icons/arrow_down.svg);\n"
"    /* qproperty-text: \">\"; */\n"
"}\n"
"#qt_calendar_prevmonth:hover, \n"
"#qt_calendar_nextmonth:hover {\n"
"    background-color: #b2d5ff;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:pressed, \n"
"#qt_calendar_nextmonth:pressed {\n"
"    background-color: #0075ff;\n"
"}\n"
"\n"
"\n"
"/* Style for month and yeat buttons #################################### */\n"
"\n"
"#qt_calendar_yearbutton {\n"
"    color: #000;\n"
"    margin:5px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    padding:5px 15px;\n"
"}\n"
"\n"
" #qt_calendar_monthbutton {\n"
"    width: 110px;\n"
"    color: #000;\n"
"    margin:5px 0px;\n"
"    border-radius: 5px;\n"
"    padding:5px 0;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover, \n"
"#qt_calendar_monthbutton:hover {\n"
"    background-color: #b2d5ff;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:pressed, \n"
"#qt_calendar_monthbutton:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"/* Style for year input lineEdit ######################################*/\n"
"\n"
"#qt_calendar_yearedit {\n"
"    min-width: 60px;\n"
"    color: #000;\n"
"    font-size: 16px;\n"
"   margin:5px;\n"
"    padding: 0 5px;\n"
"}\n"
"\n"
"/* Style for year change buttons ######################################*/\n"
"\n"
"#qt_calendar_yearedit::up-button { \n"
"    image: url(:/icons/arrow-151-48.ico);\n"
"    subcontrol-position: right;\n"
"    height: 30px;\n"
"    width: 30px;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button { \n"
"    image: url(:/icons/arrow-213-48.ico);\n"
"    subcontrol-position: left; \n"
"    height: 30px;\n"
"    width: 30px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button, \n"
"#qt_calendar_yearedit::up-button {\n"
"    width:10px;\n"
"    padding: 0px 5px;\n"
"    border-radius:3px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button:hover, \n"
"#qt_calendar_yearedit::up-button:hover {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"/* Style for month select menu ##################################### */\n"
"\n"
"#calendarWidget QToolButton QMenu {\n"
"     background-color: #fff;\n"
"    border: 1px solid #f3f3f3;\n"
"\n"
"}\n"
"#calendarWidget QToolButton QMenu::item {\n"
"    padding: 5px 20px;\n"
"    font-size: 14px;\n"
"}\n"
" #calendarWidget QToolButton QMenu::item:selected:enabled {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#calendarWidget QToolButton::menu-indicator {\n"
"    /* Remove toolButton arrow */\n"
"      /*image: none; */\n"
"    nosubcontrol-origin: margin;\n"
"    subcontrol-position: right center;\n"
"    margin-top: 10px;\n"
"    width:20px;\n"
"\n"
"}\n"
"\n"
"/* Style for calendar table ########################################## */\n"
"#qt_calendar_calendarview {\n"
"    /* Remove the selected dashed box */\n"
"    outline: 0px;\n"
"    border-top: 0px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item {\n"
"     border-radius:5px;\n"
"    margin: 1px;    \n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover {\n"
"    background-color:#b2d5ff;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected {\n"
"    background-color: #0075ff; \n"
"    color: #fff;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 15, -1, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setMinimumSize(QtCore.QSize(335, 0))
        self.calendarWidget.setMaximumSize(QtCore.QSize(335, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clear_btn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        self.clear_btn.setFont(font)
        self.clear_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_2.addWidget(self.clear_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.now_btn = QtWidgets.QPushButton(Dialog)
        self.now_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.now_btn.setObjectName("now_btn")
        self.horizontalLayout_2.addWidget(self.now_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 15, -1, 25)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setMinimumSize(QtCore.QSize(80, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setMinimumSize(QtCore.QSize(80, 0))
        self.listWidget_2.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, 15)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pm_btn = QtWidgets.QPushButton(Dialog)
        self.pm_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pm_btn.setCheckable(True)
        self.pm_btn.setChecked(True)
        self.pm_btn.setObjectName("pm_btn")
        self.verticalLayout_2.addWidget(self.pm_btn)
        self.am_btn = QtWidgets.QPushButton(Dialog)
        self.am_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.am_btn.setCheckable(True)
        self.am_btn.setObjectName("am_btn")
        self.verticalLayout_2.addWidget(self.am_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.clear_btn.setText(_translate("Dialog", "Clear"))
        self.now_btn.setText(_translate("Dialog", "Now"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "01"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "02"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "03"))
        item = self.listWidget.item(3)
        item.setText(_translate("Dialog", "04"))
        item = self.listWidget.item(4)
        item.setText(_translate("Dialog", "05"))
        item = self.listWidget.item(5)
        item.setText(_translate("Dialog", "06"))
        item = self.listWidget.item(6)
        item.setText(_translate("Dialog", "07"))
        item = self.listWidget.item(7)
        item.setText(_translate("Dialog", "08"))
        item = self.listWidget.item(8)
        item.setText(_translate("Dialog", "09"))
        item = self.listWidget.item(9)
        item.setText(_translate("Dialog", "10"))
        item = self.listWidget.item(10)
        item.setText(_translate("Dialog", "11"))
        item = self.listWidget.item(11)
        item.setText(_translate("Dialog", "12"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Dialog", "00"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Dialog", "01"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("Dialog", "02"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("Dialog", "03"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("Dialog", "04"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("Dialog", "05"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("Dialog", "06"))
        item = self.listWidget_2.item(7)
        item.setText(_translate("Dialog", "07"))
        item = self.listWidget_2.item(8)
        item.setText(_translate("Dialog", "08"))
        item = self.listWidget_2.item(9)
        item.setText(_translate("Dialog", "09"))
        item = self.listWidget_2.item(10)
        item.setText(_translate("Dialog", "10"))
        item = self.listWidget_2.item(11)
        item.setText(_translate("Dialog", "11"))
        item = self.listWidget_2.item(12)
        item.setText(_translate("Dialog", "12"))
        item = self.listWidget_2.item(13)
        item.setText(_translate("Dialog", "13"))
        item = self.listWidget_2.item(14)
        item.setText(_translate("Dialog", "14"))
        item = self.listWidget_2.item(15)
        item.setText(_translate("Dialog", "15"))
        item = self.listWidget_2.item(16)
        item.setText(_translate("Dialog", "16"))
        item = self.listWidget_2.item(17)
        item.setText(_translate("Dialog", "17"))
        item = self.listWidget_2.item(18)
        item.setText(_translate("Dialog", "18"))
        item = self.listWidget_2.item(19)
        item.setText(_translate("Dialog", "19"))
        item = self.listWidget_2.item(20)
        item.setText(_translate("Dialog", "20"))
        item = self.listWidget_2.item(21)
        item.setText(_translate("Dialog", "21"))
        item = self.listWidget_2.item(22)
        item.setText(_translate("Dialog", "22"))
        item = self.listWidget_2.item(23)
        item.setText(_translate("Dialog", "23"))
        item = self.listWidget_2.item(24)
        item.setText(_translate("Dialog", "24"))
        item = self.listWidget_2.item(25)
        item.setText(_translate("Dialog", "25"))
        item = self.listWidget_2.item(26)
        item.setText(_translate("Dialog", "25"))
        item = self.listWidget_2.item(27)
        item.setText(_translate("Dialog", "27"))
        item = self.listWidget_2.item(28)
        item.setText(_translate("Dialog", "28"))
        item = self.listWidget_2.item(29)
        item.setText(_translate("Dialog", "29"))
        item = self.listWidget_2.item(30)
        item.setText(_translate("Dialog", "30"))
        item = self.listWidget_2.item(31)
        item.setText(_translate("Dialog", "31"))
        item = self.listWidget_2.item(32)
        item.setText(_translate("Dialog", "32"))
        item = self.listWidget_2.item(33)
        item.setText(_translate("Dialog", "33"))
        item = self.listWidget_2.item(34)
        item.setText(_translate("Dialog", "34"))
        item = self.listWidget_2.item(35)
        item.setText(_translate("Dialog", "35"))
        item = self.listWidget_2.item(36)
        item.setText(_translate("Dialog", "36"))
        item = self.listWidget_2.item(37)
        item.setText(_translate("Dialog", "37"))
        item = self.listWidget_2.item(38)
        item.setText(_translate("Dialog", "38"))
        item = self.listWidget_2.item(39)
        item.setText(_translate("Dialog", "39"))
        item = self.listWidget_2.item(40)
        item.setText(_translate("Dialog", "40"))
        item = self.listWidget_2.item(41)
        item.setText(_translate("Dialog", "41"))
        item = self.listWidget_2.item(42)
        item.setText(_translate("Dialog", "42"))
        item = self.listWidget_2.item(43)
        item.setText(_translate("Dialog", "43"))
        item = self.listWidget_2.item(44)
        item.setText(_translate("Dialog", "44"))
        item = self.listWidget_2.item(45)
        item.setText(_translate("Dialog", "45"))
        item = self.listWidget_2.item(46)
        item.setText(_translate("Dialog", "46"))
        item = self.listWidget_2.item(47)
        item.setText(_translate("Dialog", "47"))
        item = self.listWidget_2.item(48)
        item.setText(_translate("Dialog", "48"))
        item = self.listWidget_2.item(49)
        item.setText(_translate("Dialog", "49"))
        item = self.listWidget_2.item(50)
        item.setText(_translate("Dialog", "50"))
        item = self.listWidget_2.item(51)
        item.setText(_translate("Dialog", "51"))
        item = self.listWidget_2.item(52)
        item.setText(_translate("Dialog", "52"))
        item = self.listWidget_2.item(53)
        item.setText(_translate("Dialog", "53"))
        item = self.listWidget_2.item(54)
        item.setText(_translate("Dialog", "54"))
        item = self.listWidget_2.item(55)
        item.setText(_translate("Dialog", "55"))
        item = self.listWidget_2.item(56)
        item.setText(_translate("Dialog", "56"))
        item = self.listWidget_2.item(57)
        item.setText(_translate("Dialog", "57"))
        item = self.listWidget_2.item(58)
        item.setText(_translate("Dialog", "58"))
        item = self.listWidget_2.item(59)
        item.setText(_translate("Dialog", "59"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.pm_btn.setText(_translate("Dialog", "PM"))
        self.am_btn.setText(_translate("Dialog", "AM"))
import resource_rc
