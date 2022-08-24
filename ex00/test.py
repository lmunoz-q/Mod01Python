import datetime

from book import Book
from recipe import Recipe

recette1 = Recipe("carpaccio", 1, 5, ["meat", "vinegar", "parmesan"], "", "starter")
recette2 = Recipe("bolognaise", 4, 200, ["meat", "onions", "celery", "carrots", "tomatoes"], "meat sauce", "lunch")
recette3 = Recipe("tiramisu", 5, 30, ["coffee", "mascarpone", "sugar", "egg"], "italian dessert", "dessert")
recette4 = Recipe("carbonara", 2, 10, ["pancetta", "egg", "pecorino", "pepper"], "creamy sauce", "lunch")
# recetteFalse = Recipe("name", 0, 0, ["ingredient1", "2"], "", "dessert") Put here everything to test

dico_test = {
	"starter": recette1,
	"lunch": recette2,
	"dessert": recette3
}

italian = Book("Italian recipes", datetime.datetime.now(), datetime.datetime.now(), dico_test)
italian.add_recipe(recette4)
print(italian)

# il manque unit test
