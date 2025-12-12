"""
the idea is to write my own Exam Shell.
This will NOT help you succeed at 42 Exam Shell.
I just want to understand how Exam Shell works, how I can check the user input.

what is the userflow?
User runs ExamShell, then receives first task
this generates Textfile with explanation of task
then can run grademe
grademe will check the written userfile for correctness
if grademe good, received next task
else must retry
"""

import sys
import shutil
import subprocess as sp

def grademe():
	bad = False
	try: content = open("your_files/helloworld.c")
	if "stdio.h" in content: bad = True
	except Exception as e: print(e); print("Bad File Input"); return

def	main():
	av = sys.argv
	ac = len(av)
	print("Welcome to Exam Shell")
	print("Here is your first task:")
	sp.run("mkdir -p your_files", shell=True)
	shutil.copy("tasks/helloworld.md", ".")
	cmd = input("(grademe):>")
	if cmd == "grademe": grademe()

if __name__ == '__main__': main()
