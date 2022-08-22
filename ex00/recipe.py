import sys


class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		try:
			if not isinstance(name, str) or name == "":
				raise TypeError("error, name must be a non empty string")
			self.name = name
			if not isinstance(cooking_lvl, int) or not 0 < cooking_lvl < 6:
				raise TypeError("error, cooking_lvl must be an integer between 1 and 5")
			self.cooking_lvl = cooking_lvl
			if not isinstance(cooking_time, int) or cooking_time < 0:
				raise TypeError("error, cooking_time must be a positive integer")
			self.cooking_time = cooking_time
			if not isinstance(ingredients, list) or not all(ingredients) or not all(isinstance(elem, str) for elem in ingredients) or not ingredients:
				raise TypeError("error, ingredients must be a non empty list containing strings")
			self.ingredients = ingredients
			if not isinstance(description, str):
				raise TypeError("error, description must be a string")
			self.description = description
			if recipe_type not in ["starter", "lunch", "dessert"]:
				raise TypeError("error, recipe_type must be a 'starter', 'lunch' or 'dessert'")
			self.recipe_type = recipe_type
		except TypeError as err:
			sys.exit(err)

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = f"The recipe is called {self.name}\nIn a scale of difficulty from 1 to 5 it's a {self.cooking_lvl}\nIt takes {self.cooking_time} minutes to cook\nthe ingredients from this recipe are : {self.ingredients}\nDescription : {self.description}\nWe can eat this recipe for {self.recipe_type}"
		return txt

