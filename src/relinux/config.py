'''
Basic configuration
@author: MiJyn
'''

import os
from relinux import fsutil

product = "Relinux"
version = 0.4
version_string = product + " version " + str(version)
about_string = product + " is a free software designed to help you make a professional-looking OS easily"

EStatus = True
IStatus = True
VStatus = True
VVStatus = True

# GUI Section
GUIStatus = True
background = "lightgrey"

# Generated section
ISOTree = ""
TempSys = ""
SysVersion = os.popen("/usr/bin/lsb_release -rs").readlines()[0].strip()
Arch = fsutil.getArch()
