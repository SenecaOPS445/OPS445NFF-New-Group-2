
import argparse
import shutil
import os
import socket
import platform
import psutil

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


    def get_ip(self):
        "Retrieval of the OS IP address"

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_add = s.getsockname()[0]
        s.close()

        return ip_add
    
if __name__ == "__main__":
        report = SystemReport()
        print("IP Address Test Output:")
        print(report.get_ip())
    