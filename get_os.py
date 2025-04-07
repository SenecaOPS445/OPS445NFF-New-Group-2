import argparse
import shutil
import os
import socket
import platform


"Creating a class called system Report, It contains the fuctions that will help the script run"

class SystemReport:
    "Initialize system report"
    def __init__(self):
        self.disk_usage = None
        self.uptime = None
        self.os = None
        self.dirs = None
        self.cpu_info = None
        self.ip = None


    def get_os(self):
        "Retrieval of the os information"

        os_name = platform.system()
        os_version = platform.version()
        os_release = platform.release()

        return f"{os_name} {os_release} (Ver: {os_version})"
    
if __name__ == "__main__":
    report = SystemReport()
    print("OS Info Test Output:")
    print(report.get_os())