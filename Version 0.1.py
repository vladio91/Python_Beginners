import getpass
import os
import platform
import sys
import time
import datetime as da

Checkup = "03:54 PM"



print("Hello ") + (getpass.getuser()) + (",")
print("you are currently working in the ") + (os.getcwd()) + (" directory.")
print("The current Python version is: ") + (platform.python_version()) + (", installed on ") + (platform.system())
print("")
print("This machine got a ")  + (platform.machine()) + (platform.processor()) + (" processor.")

def Check():
    now = da.datetime.now().strftime("%I:%M %p")
    print("Testing ...")
    while True:
        if now == Checkup:
            print("Pizza Time")

            time.sleep(60)
            Check()
        else:
            print("Not Yet ready")
            print("it is now ") + (now) + (" The Next Pizza Time will be at ") + (Checkup)
            time.sleep(60)
            Check()
Check()


print("Version 0.1.1 Alpha")
