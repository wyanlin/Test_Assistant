
import serial
import serial.tools.list_ports
import yaml
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox

from common.log import Log
from ui.cpSettings import Ui_Dialog


class CP_settings(Ui_Dialog, QDialog):
    # 让多窗口之间传递信号，刷新主窗口信息
    my_Signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)
        self.log = Log(__name__).getlog()
        icon = 'D:\\ihblu\\wyrepo\\Test_Assistant\\img\\icon.ico'
        self.setWindowIcon(QIcon(icon))
        self.__load_CP_config()
        self.init()

    def init(self):
        self.log.info("######>>> Init Default settings Dialog")

        self.Btn_settings_save.clicked.connect(self.__write_config)
        self.Btn_settings_save.clicked.connect(self.close)
        self.Btn_settings_cancel.clicked.connect(self.close)
        self.Btn_TT_browse.clicked.connect(self.TT_browse)
        self.Btn_Trace_browse.clicked.connect(self.Trace_browse)
        self.Btn_refresh_port.clicked.connect(self.port_check)


    def sendEditContent(self):
        content = '1'
        self.my_Signal.emit(content)

    def closeEvent(self, event):
        self.sendEditContent()

    def TT_browse(self, Filepath):
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "C:/", "*.exe")  # 起始路径
        self.Ledit_TT_path.setText(m[0])

    def Trace_browse(self, Filepath):
        # m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "C:/", "*.exe")  # 起始路径
        self.Ledit_Trace_path.setText(m[0])

    def msg_box(self, title, msg):
        return QMessageBox(QMessageBox.Warning, title, msg)

    def __load_CP_config(self):

        with open('config/config.yml', 'r', encoding='utf-8') as f:
            content = yaml.load(f.read(), yaml.FullLoader)

            self.Ledit_calledNumber.setText(content['config_call']['call_number'])
            self.Ledit_callInterval.setText(content['config_call']['call_interval'])
            self.Ledit_TT_path.setText(content['CP_test']['TT_path'])
            self.Ledit_Trace_path.setText(content['CP_test']['Trace_path'])
        self.log.info("load CP settings")


    def __write_config(self):
        with open('config/config.yml', 'r', encoding='utf-8') as f:
            content = yaml.load(f.read(), yaml.FullLoader)
            if self.Ledit_calledNumber.text().isdigit():
                content['CP_test']['call_number'] = self.Ledit_calledNumber.text()
            if self.Ledit_callInterval.text().isdigit():
                content['CP_test']['call_interval'] = self.Ledit_callInterval.text()

            content['CP_test']['TT_path'] = self.Ledit_TT_path.text()
            content['CP_test']['Trace_path'] = self.Ledit_Trace_path.text()

        with open('config/config.yml', 'w', encoding='utf-8') as wf:
            yaml.dump(content, wf, Dumper=yaml.SafeDumper)
        self.log.info("write CP config, calledName: %s, calledInterval: %s\nTT path: %s\nTrace path: %s\nCOM: %s" %
                      (self.Ledit_calledNumber.text(), self.Ledit_callInterval.text(),
                       self.Ledit_TT_path.text(), self.Ledit_Trace_path.text(),
                       self.ComboBox_serial_port.currentText()))


    def port_check(self):
        """
        CP 检测连接log的端口
        :return: None
        """
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.ComboBox_serial_port.clear()
        for port in port_list:
            res = ' '.join(port.description.split(' ')[1:])
            # self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.ComboBox_serial_port.addItem(res)

        self.log.debug("Port list:%s" % self.Com_Dict)
        if len(self.Com_Dict) == 0:
            self.ComboBox_serial_port.setCurrentText("无串口")