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

if __name__ == "__main__":
    report = SystemReport()
    print(report.get_dir())