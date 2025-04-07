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

if __name__ == "__main__":
    report = SystemReport()
    print(report.get_cpu_info())