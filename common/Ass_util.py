import re
import subprocess
import sys

# WIN32 API
IS_WIN32 = 'win32' in str(sys.platform).lower()

def subprocess_getoutput(*args):
    #also works for Popen. It creates a new *hidden* window, so it will work in frozen apps (.exe).
    if IS_WIN32:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        # kwargs['startupinfo'] = startupinfo
    retcode = subprocess.getoutput(*args)
    return retcode


def subprocess_call(*args, **kwargs):
    #also works for Popen. It creates a new *hidden* window, so it will work in frozen apps (.exe).
    if IS_WIN32:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        kwargs['startupinfo'] = startupinfo
    retcode = subprocess.call(*args, **kwargs)
    return retcode

def dev():
    """
    检测设备，有设备，返回设备名；无设备，返回0
    :return: 设备名
    :return: 0
    """
    pattern = re.compile('[a-zA-Z0-9]+\sdevice$')
    devices_list = subprocess_getoutput('adb devices').strip().split('\n')
    devName = devices_list[-1].split('\t')[0]
    devices_count = 0
    for d in devices_list:
        r = pattern.match(d)
        if r:
            devices_count += 1
    if devices_count == 0:
        return 0
    elif devices_count == 1:
        return devName
    else:
        return 2

def recv_to_bottom(self):
    # 获取到text光标
    textCursor = self.CP_recv_textBrowser.textCursor()
    # 滚动到底部
    textCursor.movePosition(textCursor.End)
    # 设置光标到text中
    self.CP_recv_textBrowser.setTextCursor(textCursor)