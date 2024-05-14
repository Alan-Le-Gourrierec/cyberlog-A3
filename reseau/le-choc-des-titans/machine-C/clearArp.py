import ctypes
import sys

def clearArp():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "arp -d *", None, 1)

clearArp()
