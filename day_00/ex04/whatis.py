import sys

if len(sys.argv) > 2 :
	print(f"AssertionError: more than one argument is provided")
elif len(sys.argv) == 2:
	try:
		value = int(sys.argv[1])
	except ValueError:
		print(f"AssertionError: argument is not an integer")
		exit()
	if value % 2 == 0 :
		print(f"I'm Even.")
	else:
		print(f"I'm Odd.")
