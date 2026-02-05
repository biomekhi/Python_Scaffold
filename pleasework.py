#!/usr/bin/env python3 
import sys 
def main(): 
name = input("Enter your name to see if it starts with a vowel")
name = name.lower()
if name.startswith(("a","e","i","o","u")):
	sys.stdout.write("Your name starts with a vowel")
elif name.startswith("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"):
	sys.stdout.write("Your name does not start with a vowel")
else:
	sys.stderr.write("Your name doesnt start with a letter")

if __name__ == '__main__':
	main()