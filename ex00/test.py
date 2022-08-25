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
		self.badKeysOfRecipes = {
			"caca": [self.recette1],
			"vomi": [self.recette2, self.recette4],
			"crachat": [self.recette3]
		}
		self.badValuesOfRecipes = {
			"starter": 3,
			"lunch": ["self.recette2", "self.recette4"],
			"dessert": [self.listBadWords]
		}

	def testCreationRecipe(self):
		"""Test if Objs are instanced properly"""
		self.assertIsInstance(self.recette1, Recipe)
		self.assertIsInstance(self.recette2, Recipe)
		self.assertIsInstance(self.recette3, Recipe)
		self.assertIsInstance(self.recette4, Recipe)
		self.assertIsInstance(self.italianBook, Book)

	def testWrongRecipeName(self):
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

	def testWrongRecipeCookingLvl(self):
		"""Test assigning incorrect type in Recipe.cooking_lvl"""

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

	def testWrongRecipeCookingTime(self):
		"""Test assigning incorrect type in Recipe.cooking_time"""
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

	def testWrongRecipeIngredients(self):
		"""Test assigning incorrect type in Recipe.ingredients"""
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

	def testWrongRecipeDescription(self):
		"""Test assigning incorrect type in Recipe.description"""
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

	def testWrongRecipe_RecipeType(self):
		"""Test assigning incorrect type in Recipe.recipe_type"""
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
		with self.assertRaises(SystemExit):
			test11 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "meat thinly sliced, and served raw", self.listBadWords)

	def testWrongBookName(self):
		"""Test assigning incorrect type in Book.name"""
		with self.assertRaises(SystemExit):
			test1 = Book(self.simpleInt, datetime.datetime.now(), datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test2 = Book(self.negativeSimpleInt, datetime.datetime.now(), datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test3 = Book(self.emptyString, datetime.datetime.now(), datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test4 = Book(self.noParameter, datetime.datetime.now(), datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test5 = Book(self.falseTest, datetime.datetime.now(), datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test6 = Book(self.trueTest, datetime.datetime.now(), datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test7 = Book(self.emptyList, datetime.datetime.now(), datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test8 = Book(self.listBadWords, datetime.datetime.now(), datetime.datetime.now(), self.listOfRecipes)

	def testWrongLastUpdate(self):
		"""Test assigning incorrect type in Book.last_update"""
		with self.assertRaises(SystemExit):
			test1 = Book("Recipes from Italia", self.simpleInt, datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test2 = Book("Recipes from Italia", self.negativeSimpleInt, datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test3 = Book("Recipes from Italia", self.intOutOfRange, datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test4 = Book("Recipes from Italia", self.negativeIntOutOfRange, datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test5 = Book("Recipes from Italia", self.emptyString, datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test6 = Book("Recipes from Italia", self.noParameter, datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test7 = Book("Recipes from Italia", self.falseTest, datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test8 = Book("Recipes from Italia", self.trueTest, datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test9 = Book("Recipes from Italia", self.emptyList, datetime.datetime.now(), self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test10 = Book("Recipes from Italia", self.listBadWords, datetime.datetime.now(), self.listOfRecipes)

	def testWrongCreationDate(self):
		"""Test assigning incorrect type in Book."""
		with self.assertRaises(SystemExit):
			test1 = Book("Recipes from Italia", datetime.datetime.now(), self.simpleInt, self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test2 = Book("Recipes from Italia", datetime.datetime.now(), self.negativeSimpleInt, self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test3 = Book("Recipes from Italia", datetime.datetime.now(), self.intOutOfRange, self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test4 = Book("Recipes from Italia", datetime.datetime.now(), self.negativeIntOutOfRange, self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test5 = Book("Recipes from Italia", datetime.datetime.now(), self.emptyString, self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test6 = Book("Recipes from Italia", datetime.datetime.now(), self.nonEmptyString, self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test7 = Book("Recipes from Italia", datetime.datetime.now(), self.noParameter, self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test8 = Book("Recipes from Italia", datetime.datetime.now(), self.falseTest, self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test9 = Book("Recipes from Italia", datetime.datetime.now(), self.trueTest, self.listOfRecipes)
		with self.assertRaises(SystemExit):
			test10 = Book("Recipes from Italia", datetime.datetime.now(), self.emptyList, self.listOfRecipes)

	def testWrongRecipeList(self):
		"""Test assigning incorrect type in Book.recipe_list"""
		with self.assertRaises(SystemExit):
			test1 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.simpleInt)
		with self.assertRaises(SystemExit):
			test2 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.negativeSimpleInt)
		with self.assertRaises(SystemExit):
			test3 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.negativeIntOutOfRange)
		with self.assertRaises(SystemExit):
			test4 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.intOutOfRange)
		with self.assertRaises(SystemExit):
			test5 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.emptyString)
		with self.assertRaises(SystemExit):
			test6 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.nonEmptyString)
		with self.assertRaises(SystemExit):
			test7 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.noParameter)
		with self.assertRaises(SystemExit):
			test8 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.falseTest)
		with self.assertRaises(SystemExit):
			test9 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.trueTest)
		with self.assertRaises(SystemExit):
			test10 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.emptyList)
		with self.assertRaises(SystemExit):
			test11 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.listBadWords)
		with self.assertRaises(SystemExit):
			test12 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.badKeysOfRecipes)
		with self.assertRaises(SystemExit):
			test13 = Book("Recipes from Italia", datetime.datetime.now(), datetime.datetime.now(), self.badValuesOfRecipes)

	def testWrongGetRecipeByName(self):
		"""Test trying to use not correctly the method get_recipe_by_name in Book"""
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipe_by_name(self.simpleInt)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipe_by_name(self.negativeSimpleInt)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipe_by_name(self.intOutOfRange)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipe_by_name(self.negativeIntOutOfRange)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipe_by_name(self.emptyString)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipe_by_name(self.nonEmptyString)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipe_by_name(self.noParameter)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipe_by_name(self.falseTest)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipe_by_name(self.trueTest)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipe_by_name(self.emptyList)

	def testWrongGetRecipeByTypes(self):
		"""Test trying to use not correctly the method get_recipe_by_type in Book"""
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipes_by_types(self.simpleInt)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipes_by_types(self.negativeSimpleInt)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipes_by_types(self.intOutOfRange)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipes_by_types(self.negativeIntOutOfRange)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipes_by_types(self.emptyString)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipes_by_types(self.nonEmptyString)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipes_by_types(self.noParameter)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipes_by_types(self.falseTest)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipes_by_types(self.trueTest)
		with self.assertRaises(SystemExit):
			test = self.italianBook.get_recipes_by_types(self.emptyList)

	def testWrongAddRecipe(self):
		"""Test trying to use not correctly the method add_recipe in Book"""
		with self.assertRaises(SystemExit):
			self.italianBook.add_recipe(self.simpleInt)
		with self.assertRaises(SystemExit):
			self.italianBook.add_recipe(self.negativeSimpleInt)
		with self.assertRaises(SystemExit):
			self.italianBook.add_recipe(self.intOutOfRange)
		with self.assertRaises(SystemExit):
			self.italianBook.add_recipe(self.negativeIntOutOfRange)
		with self.assertRaises(SystemExit):
			self.italianBook.add_recipe(self.emptyString)
		with self.assertRaises(SystemExit):
			self.italianBook.add_recipe(self.nonEmptyString)
		with self.assertRaises(SystemExit):
			self.italianBook.add_recipe(self.noParameter)
		with self.assertRaises(SystemExit):
			self.italianBook.add_recipe(self.falseTest)
		with self.assertRaises(SystemExit):
			self.italianBook.add_recipe(self.trueTest)
		with self.assertRaises(SystemExit):
			self.italianBook.add_recipe(self.emptyList)
		with self.assertRaises(SystemExit):
			self.italianBook.add_recipe(self.listBadWords)
		with self.assertRaises(SystemExit):
			self.italianBook.add_recipe(Recipe(6969, "trois", "6 minutes", 3, "", self.listOfRecipes))


if __name__ == '__main__':
	unittest.main()
