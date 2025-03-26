#!/usr/bin/env python3

### OPS445NFF
### Instructor: Eric Brauer
### Winter 2025 Assignment 2
### ASSIGNMENT 2: System Reporting and Metrics Script
### Group 2 Members:Jude Owusu - 103399176 


import argparse
import os

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
        

        return
    
    def get_uptime(self):
        

        return
    
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