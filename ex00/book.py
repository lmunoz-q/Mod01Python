import datetime
import sys
from ex00.recipe import Recipe


class Book:
	def __init__(self, name, last_update, creation_date, recipe_list):
		try:
			if not isinstance(name, str) or name == "":
				raise TypeError("error, name must be a non empty string")
			self.name = name
			if not isinstance(last_update, datetime.date):
				raise TypeError("error, last_update must be a datatime type")
			self.last_update = last_update
			if not isinstance(creation_date, datetime.date):
				raise TypeError("error, creation_date must be a datatime type")
			self.creation_date = creation_date
			if not all(key in ["starter", "lunch", "dessert"] for key in recipe_list.keys()):
				raise TypeError("error, the dictionary not contain ['starter', 'lunch', dessert] as a key value")
			self.recipe_list = dict(recipe_list)
		except TypeError as err:
			sys.exit(err)

		def get_recipe_by_name(self, name):
			"""Prints a recipe with the name \texttt{name} and returns the instance"""
			print(f"The recipe by name is : {name}")

		def get_recipes_by_types(self, recipe_type):
			"""Get all recipe names for a given recipe_type"""
			print("the recipe by type is :")

		def add_recipe(self, recipe):
			"""Add a recipe to the book and update last_update"""
			if not isinstance(recipe, Recipe):
				print("recipe is not a Recipe type")

