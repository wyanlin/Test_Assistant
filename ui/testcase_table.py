# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testcase_table.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Testcase_table(object):
    def setupUi(self, Testcase_table):
        Testcase_table.setObjectName("Testcase_table")
        Testcase_table.resize(510, 724)
        Testcase_table.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Testcase_table)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Btn_cancel_case = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Btn_cancel_case.setFont(font)
        self.Btn_cancel_case.setObjectName("Btn_cancel_case")
        self.gridLayout.addWidget(self.Btn_cancel_case, 1, 3, 1, 1)
        self.Btn_set_case = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Btn_set_case.setFont(font)
        self.Btn_set_case.setObjectName("Btn_set_case")
        self.gridLayout.addWidget(self.Btn_set_case, 1, 0, 1, 1)
        self.TreeWidget_case = QtWidgets.QTreeWidget(self.centralwidget)
        self.TreeWidget_case.setObjectName("TreeWidget_case")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.TreeWidget_case.headerItem().setFont(0, font)
        self.TreeWidget_case.headerItem().setBackground(0, QtGui.QColor(255, 170, 127))
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.TreeWidget_case.headerItem().setForeground(0, brush)

        item_0 = QtWidgets.QTreeWidgetItem(self.TreeWidget_case)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item_1.setFont(0, font)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item_1.setFont(0, font)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item_1.setFont(0, font)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item_1.setFont(0, font)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)

        item_0 = QtWidgets.QTreeWidgetItem(self.TreeWidget_case)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_1.setFont(0, font)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_1.setFont(0, font)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_0 = QtWidgets.QTreeWidgetItem(self.TreeWidget_case)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        # item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_1.setFont(0, font)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        # item_1.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_1.setFont(0, font)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)

        item_bt_test = QtWidgets.QTreeWidgetItem(self.TreeWidget_case)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_bt_test.setFont(0, font)
        item_bt_test.setText(0, "蓝牙测试")
        item_bt_test.setCheckState(0, QtCore.Qt.Unchecked)

        item_bt_conn = QtWidgets.QTreeWidgetItem(item_bt_test)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_bt_conn.setFont(0, font)
        item_bt_conn.setText(0, "蓝牙连接测试")
        item_bt_conn.setCheckState(0, QtCore.Qt.Unchecked)

        item_onoff = QtWidgets.QTreeWidgetItem(item_bt_test)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_onoff.setFont(0, font)
        item_onoff.setText(0, "蓝牙开关测试")
        item_onoff.setCheckState(0, QtCore.Qt.Unchecked)

        self.gridLayout.addWidget(self.TreeWidget_case, 0, 0, 1, 4)
        self.Btn_save_case = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Btn_save_case.setFont(font)
        self.Btn_save_case.setObjectName("Btn_save_case")
        self.gridLayout.addWidget(self.Btn_save_case, 1, 2, 1, 1)
        Testcase_table.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Testcase_table)
        self.statusbar.setObjectName("statusbar")
        Testcase_table.setStatusBar(self.statusbar)

        self.retranslateUi(Testcase_table)
        QtCore.QMetaObject.connectSlotsByName(Testcase_table)

    def load_case(self):
        pass

    def retranslateUi(self, Testcase_table):
        _translate = QtCore.QCoreApplication.translate
        Testcase_table.setWindowTitle(_translate("Testcase_table", "用例表"))

        self.TreeWidget_case.setProperty("setItemWidget", _translate("Testcase_table", "hello"))
        self.TreeWidget_case.headerItem().setText(0, _translate("Testcase_table", "用例标题"))
        __sortingEnabled = self.TreeWidget_case.isSortingEnabled()
        self.TreeWidget_case.setSortingEnabled(False)
        self.TreeWidget_case.topLevelItem(0).setText(0, _translate("Testcase_table", "通话测试"))
        self.TreeWidget_case.topLevelItem(0).child(0).setText(0, _translate("Testcase_table", "主叫主挂"))
        self.TreeWidget_case.topLevelItem(0).child(1).setText(0, _translate("Testcase_table", "主叫被挂"))
        self.TreeWidget_case.topLevelItem(0).child(2).setText(0, _translate("Testcase_table", "主叫拒接"))
        self.TreeWidget_case.topLevelItem(0).child(3).setText(0, _translate("Testcase_table", "主叫未接"))
        self.TreeWidget_case.topLevelItem(1).setText(0, _translate("Testcase_table", "卡测试"))
        self.TreeWidget_case.topLevelItem(1).child(0).setText(0, _translate("Testcase_table", "SIM卡检测"))
        self.TreeWidget_case.topLevelItem(1).child(1).setText(0, _translate("Testcase_table", "SD卡检测"))
        self.TreeWidget_case.topLevelItem(2).setText(0, _translate("Testcase_table", "WIFI测试"))
        self.TreeWidget_case.topLevelItem(2).child(0).setText(0, _translate("Testcase_table", "WIFI开关"))
        self.TreeWidget_case.topLevelItem(2).child(1).setText(0, _translate("Testcase_table", "WIFI连接"))
        # self.TreeWidget_case.topLevelItem(3).setText(0, _translate("Testcase_table", "蓝牙测试"))
        # self.TreeWidget_case.topLevelItem(3).child(0).setText(0, _translate("Testcase_table", "蓝牙开关"))
        # self.TreeWidget_case.topLevelItem(3).child(1).setText(0, _translate("Testcase_table", "蓝牙连接"))

        self.TreeWidget_case.setSortingEnabled(__sortingEnabled)
        self.Btn_save_case.setText(_translate("Testcase_table", "保存"))
        self.Btn_cancel_case.setText(_translate("Testcase_table", "取消"))
        self.Btn_set_case.setText(_translate("Testcase_table", "配置"))
