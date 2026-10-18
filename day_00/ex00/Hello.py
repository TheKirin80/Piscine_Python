ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# your code here
ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")
# “Un set en Python n’a pas d’ordre — donc son affichage ne doit
# jamais être utilisé pour valider une logique.”
ft_set = {"Hello", "Paris!"}
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
