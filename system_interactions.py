import os
import subprocess

class SystemInteractions:
    def shutdown_computer(self):
        if os.name == 'nt':
            os.system('shutdown /s /f /t 0')
        elif os.name == 'posix':
            os.system('sudo shutdown -h now')

    def restart_computer(self):
        if os.name == 'nt':
            os.system('shutdown /r /f /t 0')
        elif os.name == 'posix':
            os.system('sudo reboot -f')