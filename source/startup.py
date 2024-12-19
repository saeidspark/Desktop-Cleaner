import winreg as reg
import os

class Startup:
    def add_to_startup(self):
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_ALL_ACCESS)
        dirpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "DesktopCleaner.exe"))
        reg.SetValueEx(key, "DesktopCleaner", 0, reg.REG_SZ, dirpath)