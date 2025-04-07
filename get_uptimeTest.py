
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



    def get_uptime(self):
        "Receive the uptime data and return it in a readable format."
        try:
            with open("/proc/uptime", 'r') as f:
                uptime_sec = float(f.readline().split()[0])
            
            days = int(uptime_sec // 86400)
            hrs = int((uptime_sec % 86400) // 3600)
            mins = int((uptime_sec % 3600) // 60)
            sec = int(uptime_sec % 60)

            return f"{days}d {hrs}h {mins}m {sec}s"
        
        except Exception as e:
            return f"Error reading uptime: {e}"

def main():
    report = SystemReport()
    uptime = report.get_uptime()
    print("System Uptime Test Output:")
    print(uptime)

if __name__ == "__main__":
    main()
