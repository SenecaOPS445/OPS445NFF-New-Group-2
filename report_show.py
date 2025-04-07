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

def report_document(self):
    """Prints the information in the system report in a readable format."""
    report_data = self.generate_report()

    # Formatting report display
    formatted_report = "\n" + "=" * 40 + "\nSYSTEM REPORT and METRICS\n" + "=" * 40 + "\n"

    for key, value in report_data.items():
        formatted_report += f"\n{key}:\n"

        # If value is a dictionary, format its key-value pairs
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                formatted_report += f"  {sub_key}: {sub_value}\n"
        else:
            formatted_report += f"{value}\n"

    print(formatted_report)
