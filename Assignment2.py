#!/usr/bin/env python3

### OPS445NFF
### Instructor: Eric Brauer
### Winter 2025 Assignment 2
### ASSIGNMENT 2: System Reporting and Metrics Script
### Group 2 Members:Jude Owusu - 103399176 


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

    def get_disk(self):
        "Retrieve and return disk usage statistics."

        total = shutil.disk_usage("/")
        used = shutil.disk_usage("/")
        free = shutil.disk_usage("/")

        # Format data for readability 
        disk_info = {
            "Total Space": f"{total // (2**30)} GB",
            "Used Space": f"{used // (2**30)} GB",
            "Free Space": f"{free // (2**30)} GB"
            }

        return disk_info
    
    def get_uptime(self):
        "Recieve the uptime data and returns in readable format."

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
    
    def get_ip(self):
        

        return
    
    def get_os(self):
        

        return
    
    def get_dir(self):
        "Retrieve and returns a list of Installed Dir"

        return
    
    
    def get_cpu_info(self):
        "Retrieve and returns CPU details"

        return
    
    def Report(self):
        "Takes information and returns all the data into a documented format"
        return {

            "Disk Usage": self.get_disk(),

            "IP address": self.get_ip(),

            "OS information": self.get_os(),

            "Uptime": self.get_uptime(),

            "Installed Directories": self.get_dir(),


            "CPU information": self.get_cpu_info()

        }
    
    def Report_show(self):
        "Prints the Information in the system report to make it readable"
        report = self.Report()

def main():
    "main function to execute the script"
    report = SystemReport()
    disk_info = report.get_disk()
    print("Disk Usage Test Output:")
    for key, value in disk_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()