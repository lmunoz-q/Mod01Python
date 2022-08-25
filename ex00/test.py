import datetime
import unittest
from book import Book
from recipe import Recipe


class Test(unittest.TestCase):
	def setUp(self) -> None:
		"""Setup <Recipe>"""
		self.recette1 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		self.recette2 = Recipe("bolognaise", 4, 200, ["meat", "onions", "celery", "carrots", "tomatoes"], "meat sauce", "lunch")
		self.recette3 = Recipe("tiramisu", 5, 30, ["coffee", "mascarpone", "sugar", "egg"], "italian dessert", "dessert")
		self.recette4 = Recipe("carbonara", 2, 10, ["pancetta", "egg", "pecorino", "pepper"], "creamy sauce", "lunch")
		self.recetteToAdd = Recipe("panna cotta", 2, 20, ["milk", "gelatin", "sugar", "fruit"], "", "dessert")
		"""Setup Dictionary for <Book>"""
		self.listOfRecipes = {
			"starter": [self.recette1],
			"lunch": [self.recette2, self.recette4],
			"dessert": [self.recette3]
		}

	def testCreationRecipe(self):
		self.assertIsInstance(self.recette1, Recipe)
		self.assertIsInstance(self.recette2, Recipe)
		self.assertIsInstance(self.recette3, Recipe)
		self.assertIsInstance(self.recette4, Recipe)

	def testWrongName(self):
		""""""


if __name__ == '__main__':
	unittest.main()
