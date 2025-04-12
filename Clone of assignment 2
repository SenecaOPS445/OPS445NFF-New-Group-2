#!/usr/bin/env python3

### OPS445NFF
### Instructor: Eric Brauer
### Winter 2025 Assignment 2
### ASSIGNMENT 2: System Reporting and Metrics Script
### Group 2 Members: Jude Owusu - 103399176 , Tania Chaudhary - 10678237

import sys
import shutil
import os
import socket
import platform

class SystemReport:
    """SystemReport class to gather and present system metrics."""

    def __init__(self):
        self.disk_usage = None
        self.uptime = None
        self.os = None
        self.dirs = None
        self.cpu_info = None
        self.ip = None

    def get_disk(self):
        """Retrieve and return disk usage statistics."""
        free, used, total = shutil.disk_usage("/")
        disk_info = {
            "Total Space": f"{total // (2**30)} GB",
            "Used Space": f"{used // (2**30)} GB",
            "Free Space": f"{free // (2**30)} GB"
        }
        return disk_info

    def get_uptime(self):
        """Return the system uptime in a readable format."""
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
        """Return the system's IP address."""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip_add = s.getsockname()[0]
            s.close()
            return ip_add
        except Exception as e:
            return f"Error retrieving IP address: {e}"

    def get_os(self):
        """Return OS information."""
        os_name = platform.system()
        os_version = platform.version()
        os_release = platform.release()
        return f"{os_name} {os_release} (Ver: {os_version})"

    def get_dir(self):
        """Check the presence of common system directories."""
        dirs = ["/bin", "/usr", "/etc", "/var", "/opt", "/home", "/sbin", "/lib", "/boot"]
        found_dirs = list(filter(os.path.isdir, dirs))

        try:
            user = os.getlogin()
        except OSError:
            user = os.environ.get("USER", "Unknown")

        return "\n".join(found_dirs) + f"\n\nCurrent User: {user}"

    def get_cpu_info(self):
        """Retrieve and return CPU details."""
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
        """Gather all system information into a dictionary."""
        report_data = {
            "Disk Usage": self.get_disk(),
            "IP Address": self.get_ip(),
            "OS Information": self.get_os(),
            "Uptime": self.get_uptime(),
            "Installed Directories": self.get_dir(),
            "CPU Information": self.get_cpu_info()
        }
        return report_data

    def report_document(self):
        """Format and print the system report."""
        report_data = self.generate_report()
        formatted_report = "\n" + "=" * 40 + "\nSYSTEM REPORT and METRICS\n" + "=" * 40 + "\n"

        for key, value in report_data.items():
            formatted_report += f"\n{key}:\n"
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    formatted_report += f"  {sub_key}: {sub_value}\n"
            else:
                formatted_report += f"{value}\n"

        print(formatted_report)

        return formatted_report  # Also return the string if saving is needed

def main():
    report = SystemReport()
    if "-save" in sys.argv:
        formatted_report = report.report_document()
        with open("system_report.txt", "w") as file:
            file.write(formatted_report)
        print("\n Report saved to system_report.txt\n")
    else:
        report.report_document()

if __name__ == "__main__":
    main()
