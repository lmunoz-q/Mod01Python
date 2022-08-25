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
		"""Setup <Book>"""
		self.italianBook = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.listOfRecipes)
		"""Setup Tests"""
		self.simpleInt = 5
		self.negativeSimpleInt = -5
		self.intOutOfRange = 4242
		self.negativeIntOutOfRange = -4242
		self.emptyString = ""
		self.nonEmptyString = "caca"
		self.noParameter = None
		self.falseTest = False
		self.trueTest = True
		self.emptyList = []
		self.listBadWords = ["caca", "vomi", "crachat"]

	def testCreationRecipe(self):
		self.assertIsInstance(self.recette1, Recipe)
		self.assertIsInstance(self.recette2, Recipe)
		self.assertIsInstance(self.recette3, Recipe)
		self.assertIsInstance(self.recette4, Recipe)
		self.assertIsInstance(self.italianBook, Book)

	def testWrongName(self):
		"""Test assigning incorrect type in Recipe.name"""

		with self.assertRaises(SystemExit):
			test1 = Recipe(self.simpleInt, 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test2 = Recipe(self.emptyString, 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test3 = Recipe(self.noParameter, 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test4 = Recipe(self.falseTest, 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test5 = Recipe(self.trueTest, 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test6 = Recipe(self.negativeSimpleInt, 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")

	def testWrongCookingLvl(self):
		"""Test assigning type incorrect in Recipe.cooking_lvl"""

		with self.assertRaises(SystemExit):
			test1 = Recipe("carpaccio", self.falseTest, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test2 = Recipe("carpaccio", self.emptyString, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test3 = Recipe("carpaccio", self.nonEmptyString, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test4 = Recipe("carpaccio", self.noParameter, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test5 = Recipe("carpaccio", self.negativeSimpleInt, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test6 = Recipe("carpaccio", self.negativeIntOutOfRange, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test6 = Recipe("carpaccio", self.intOutOfRange, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")

	def testWrongCookingTime(self):
		"""Test assigning type incorrect in Recipe.cooking_time"""
		with self.assertRaises(SystemExit):
			test1 = Recipe("carpaccio", 1, self.falseTest, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test2 = Recipe("carpaccio", 1, self.emptyString, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test3 = Recipe("carpaccio", 1, self.nonEmptyString, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test4 = Recipe("carpaccio", 1, self.noParameter, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test5 = Recipe("carpaccio", 1, self.negativeSimpleInt, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test6 = Recipe("carpaccio", 1, self.negativeIntOutOfRange, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test6 = Recipe("carpaccio", 1, self.falseTest, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")

	def testWrongIngredients(self):
		"""Test assigning type incorrect in Recipe.ingredients"""
		with self.assertRaises(SystemExit):
			test1 = Recipe("carpaccio", 1, 5, self.simpleInt, "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test2 = Recipe("carpaccio", 1, 5, self.negativeSimpleInt, "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test3 = Recipe("carpaccio", 1, 5, self.intOutOfRange, "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test4 = Recipe("carpaccio", 1, 5, self.negativeIntOutOfRange, "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test5 = Recipe("carpaccio", 1, 5, self.emptyString, "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test6 = Recipe("carpaccio", 1, 5, self.nonEmptyString, "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test7 = Recipe("carpaccio", 1, 5, self.noParameter, "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test8 = Recipe("carpaccio", 1, 5, self.falseTest, "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test9 = Recipe("carpaccio", 1, 5, self.trueTest, "meat thinly sliced, and served raw", "starter")
		with self.assertRaises(SystemExit):
			test10 = Recipe("carpaccio", 1, 5, self.emptyList, "meat thinly sliced, and served raw", "starter")

	def testWrongDescription(self):
		"""Test assigning type incorrect in Recipe.description"""
		with self.assertRaises(SystemExit):
			test1 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], self.simpleInt, "starter")
		with self.assertRaises(SystemExit):
			test2 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], self.negativeSimpleInt, "starter")
		with self.assertRaises(SystemExit):
			test3 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], self.intOutOfRange, "starter")
		with self.assertRaises(SystemExit):
			test4 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], self.noParameter, "starter")
		with self.assertRaises(SystemExit):
			test5 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], self.falseTest, "starter")
		with self.assertRaises(SystemExit):
			test6 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], self.trueTest, "starter")
		with self.assertRaises(SystemExit):
			test7 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], self.emptyList, "starter")

	def testWrongRecipeType(self):
		with self.assertRaises(SystemExit):
			test1 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", self.simpleInt)
		with self.assertRaises(SystemExit):
			test2 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", self.negativeSimpleInt)
		with self.assertRaises(SystemExit):
			test3 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", self.intOutOfRange)
		with self.assertRaises(SystemExit):
			test4 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", self.negativeIntOutOfRange)
		with self.assertRaises(SystemExit):
			test5 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", self.emptyString)
		with self.assertRaises(SystemExit):
			test6 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", self.nonEmptyString)
		with self.assertRaises(SystemExit):
			test7 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", self.noParameter)
		with self.assertRaises(SystemExit):
			test8 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", self.falseTest)
		with self.assertRaises(SystemExit):
			test9 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", self.trueTest)
		with self.assertRaises(SystemExit):
			test10 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", self.emptyList)


		"""self.simpleInt = 5
		self.negativeSimpleInt = -5
		self.intOutOfRange = 4242
		self.negativeIntOutOfRange = -4242
		self.emptyString = ""
		self.nonEmptyString = "caca"
		self.noParameter = None
		self.falseTest = False
		self.trueTest = True
		self.emptyList = []
		self.listBadWords = ["caca", "vomi", "crachat"]
		Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", "starter")"""


if __name__ == '__main__':
	unittest.main()
