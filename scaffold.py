#!/usr/bin/env python3

import os 
import sys

def main():
	out_file = input("Enter the name of the output file: ")
	exist = os.path.exists(out_file)
	if exist == True:
		sys.stderr.write("File exists would you like to overwrite the file? ")
		overwrite = input("Please answer with yes or no: ")
		if overwrite in ("yes"):
			new_file(out_file)
		else:
			return		
	else:
		new_file(out_file)


def new_file(out_file):
	with open(out_file, "w+", newline = '\n') as f:
		sys.stdout = f
		sys.stdout.write("#!/usr/bin/env python3 \n")
		sys.stdout.write("import sys \n")
		sys.stdout.write("def main(): \n")
		sys.stdout.write('name = input("Enter your name to see if it starts with a vowel")\n')
		sys.stdout.write("name = name.lower()\n")
		sys.stdout.write('if name.startswith(("a","e","i","o","u")):\n')
		sys.stdout.write('	sys.stdout.write("Your name starts with a vowel")\n')
		sys.stdout.write('elif name.startswith("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"):\n')
		sys.stdout.write('	sys.stdout.write("Your name does not start with a vowel")\n')
		sys.stdout.write('else:\n')
		sys.stdout.write('	sys.stderr.write("Your name doesnt start with a letter")\n')
		sys.stdout.write("\n")
		sys.stdout.write("if __name__ == '__main__':\n	main()") 
		os.chmod(out_file, 0o755)
		










if __name__ == '__main__':
	main()