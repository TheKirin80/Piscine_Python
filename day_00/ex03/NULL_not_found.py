def NULL_not_found(object: any) -> int:
	match object:
		case None:
			print(f"Nothing: {object} <class 'NoneType'>")
			return 0
		case _ if object != object: # pour savoir si c'est le Not a Number en float sans fonction il faut verifier si il est different de lui meme, c'est seulement le cas pour le NaN
			print(f"Cheese: {object} <class 'float'>")
			return 0
		case False: # On est oblige de mettre le cas False avant le 0 sinon False est considere comme 0 et sort dans le mauvais case
			print(f"Fake: {object} <class 'bool'>")
			return 0
		case 0:
			print(f"Zero: {object} <class 'int'>")
			return 0
		case "":
			print(f"Empty:{object} <class 'str'>")
			return 0
		case _:
			print(f"Type not Found")
			return 1