# *********************************************************************
# This file illustrates how to execute a command and get it's output
# *********************************************************************
# commands library removed in python3, use subprocess instead
import subprocess

# Run ls command, get output, and print it
for line in subprocess.getstatusoutput('ls -l'):
	print(line)



