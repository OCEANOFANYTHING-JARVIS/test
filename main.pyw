import os

def openCmd():
    cmd = "C:\\Windows\\system32\\cmd.exe"
    os.startfile(cmd)
    
def closeCmd():
    os.system("taskkill /f /im cmd.exe")
