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

    def get_ip(self):
        "Retrieval of the OS IP address"

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_add = s.getsockname()[0]
        s.close()

        return ip_add
    
    def get_os(self):
        "Retrieval of the os information"

        os_name = platform.system()
        os_version = platform.version()
        os_release = platform.release()

        return f"{os_name} {os_release} (Ver: {os_version})"
    
   
    def get_dir(self):
        "Check the directories that are presently installed"

        dirs = ["/bin", "/usr", "/etc", "/var", "/opt", "/home", "/sbin", "/lib", "/boot"]

        found = filter(os.path.isdir, dirs)

        try:
            user = os.getlogin()
        except OSError:
            #IF os.getlogin fails or an error is encountered 
            user = os.environ.get("USER", " Unknown")

        return f"Installed Directories:\n" + "\n".join(dirs) + f"\n\nCurrent User: {user}"
    
    
    def get_cpu_info(self):
        "Retrieve and return CPU details"
        try:
            with open("/proc/cpuinfo", "r") as f:
                lines = f.readlines()
            
            cpu_model = None
            cpu_cores = 0

            for line in lines:
                if "model name" in line.lower() and cpu_model is None:
                    parts = line.split(":")
                    if len(parts) > 1:
                        cpu_model = parts[1].strip()
                if line.lower().startswith("processor"):
                    cpu_cores += 1
            
            if cpu_model is None:
                cpu_model = "Unknown"

            return f"Model: {cpu_model}\nCores: {cpu_cores}"
        
        except Exception as e:
            return f"Error retrieving CPU info: {e}"

    
    def generate_report(self):
        "Takes information and returns all the data into a documented format"
        return {

            "Disk Usage": self.get_disk(),

            "IP address": self.get_ip(),

            "OS information": self.get_os(),

            "Uptime": self.get_uptime(),

            "Installed Directories": self.get_dir(),


            "CPU information": self.get_cpu_info()

        }
    
    def report_show(self):
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