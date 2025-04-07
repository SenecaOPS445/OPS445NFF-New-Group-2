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

    def get_disk(self):
        "Retrieve and return disk usage statistics."

        free, used, total = shutil.disk_usage("/")
       
        # Format data for readability 
        disk_info = {
            "Total Space": f"{total // (2**30)} GB",
            "Used Space": f"{used // (2**30)} GB",
            "Free Space": f"{free // (2**30)} GB"
            }

        return disk_info
    
def main():
    "main function to execute the script"
    report = SystemReport()
    disk_info = report.get_disk()
    print("Disk Usage Test Output:")
    for key, value in disk_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()