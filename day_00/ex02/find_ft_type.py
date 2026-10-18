def all_thing_is_obj(object: any) -> int:
	match object:
		case list():
			print(f"List : <class 'list'>")
		case tuple():
			print(f"Tuple : <class 'tuple'>")
		case set():
			print(f"Set : <class 'set'>")
		case dict():
			print(f"Dict : <class 'dict'>")
		case str():
			print(f"{object} is in the kitchen : <class 'str'>")
		case _: # Le _ permet de definir un comportement par defaut
			print("Type not found")
	return (42)
