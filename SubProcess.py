__author__ = 'davidnovogrodsky_wrk'
# the os module allows Python to talk to OS
# subprocess allows shell to talk to Python
import subprocess

# good idea to store the result code from the process
# useful for flow control
resultCode = subprocess.call('ls',shell=True)

## this stores the value from the OS
output = subprocess.check_output('ls',shell=True)
print(output)
print("\n\n\n")
print(resultCode)

