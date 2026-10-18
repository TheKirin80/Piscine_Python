import sys

if len(sys.argv) < 2:
	pass
else:
	try:
		# assert permet de donner une verite et envoye au except si la verite est fausse
		assert len(sys.argv) == 2, "more than one argument is provided"
		try:
			value = int(sys.argv[1])
		except ValueError:
			raise AssertionError("argument is not an integer")
		else:
			# Le bloc try except else permet de lancer le code de else si 
			# aucun flag n'a ete leve
			if value % 2 == 0 :
				print("I'm Even.")
			else:
				print("I'm Odd.")
	except AssertionError as error:
		print(f"AssertionError: {error}")

