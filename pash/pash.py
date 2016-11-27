import sys
import pexpect


def pash():
    print("This is a test")


class spawn(pexpect.spawn):
    def __init__(self):
        pexpect.spawn.__init__(self, "/bin/bash")
        self.logfile = sys.stdout

    def sendlinebl(self, s=''):
        return self.sendline(s)
